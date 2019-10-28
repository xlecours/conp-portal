# -*- coding: utf-8 -*-
"""Threading Module

Module that contains the threaded pipeline searching functions
"""
from boutiques.searcher import Searcher
from boutiques.puller import Puller
import threading
import json
import os
import logging
import requests
from datalad import api
from datalad.api import Dataset as DataladDataset

class UpdatePipelineData(threading.Thread):
    """
        Class that handles the threaded updating of the Pipeline
        registrty from Zenodo
    """
    def __init__(self, path):
        super(UpdatePipelineData, self).__init__()
        if not os.path.exists('logs'):
            os.makedirs('logs')
        logging.basicConfig(filename='logs/update_pipeline_thread.log', level=logging.INFO)
        self.cache_dir = path

    def run(self):
        try:
            # if cache directory doesn't exist then create it
            if not os.path.exists(self.cache_dir):
                os.makedirs(self.cache_dir)

            # first search for all descriptors
            searcher = Searcher(query="", max_results=100, no_trunc=True)
            all_descriptors = searcher.search()

            # then pull every single descriptor
            all_descriptor_ids = list(map(lambda x: x["ID"], all_descriptors))
            Puller(all_descriptor_ids).pull()

            # fetch every single descriptor into one file
            detailed_all_descriptors = [
                json.load(open(os.path.join(self.cache_dir,
                                            descriptor["ID"].replace(".", "-") + ".json"),
                          "r"))
                for descriptor in all_descriptors
            ]

            # store data in cache
            with open(os.path.join(self.cache_dir,
                                   "all_descriptors.json"),
                      "w") as f:
                json.dump(all_descriptors, f, indent=4)

            with open(os.path.join(self.cache_dir,
                                   "detailed_all_descriptors.json"),
                      "w") as f:
                json.dump(detailed_all_descriptors, f, indent=4)

        except Exception as e:
            logging.exception("An exception occurred in the thread.")


class UpdateDatasets(threading.Thread):
    def __init__(self, path):
        super(UpdateDatasets, self).__init__()
        if not os.path.exists('logs'):
            os.makedirs('logs')
        logging.basicConfig(filename='logs/update_datasets_thread.log', level=logging.INFO)
        self.datasetspath = path

    def find(self, pattern, path):
        import fnmatch
        result = []
        for file in os.listdir(path):
            if fnmatch.fnmatch(file, pattern):
                result.append(file)
        return result

    def run(self):
        from app import db
        from app.models import User, Dataset, DatasetStats
        from datalad import api
        from datalad.api import Dataset as DataladDataset
        from datetime import datetime

        try:
            '''
             Instanciate the CONP dataset
            '''
            d = DataladDataset(path=self.datasetspath)
            if not d.is_installed():
                d.install(path='', recursive=True)

            d.install(path='', recursive=True)

            try:
                d.update(path='')
            except Exception as e:
                logging.exception("An exception occurred in datalad update")

            for ds in d.subdatasets():
                print(ds['gitmodule_name'])
                subdataset = DataladDataset(path=ds['path'])
                if not subdataset.is_installed():
                    subdataset.install(path='', recursive=True)

                dataset = Dataset(
                    download_path=ds['path'],
                    name=ds['gitmodule_name'],
                    date_created=datetime.utcnow(),
                    date_updated=datetime.utcnow(),
                )
                db.session.add(dataset)

            db.session.commit()

        except Exception as e:
            logging.exception("An exception occurred in the thread.")
