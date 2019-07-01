
Highcharts.chart('chart', {

    chart: {
        type: 'column',
        styledMode: true,
        backgroundColor: '#FFF'
    },
    credits: {
        enabled: false
    },

    title: {
        text: 'Number of Datasets and Pipelines in 2019'
    },

    yAxis: [{
        className: 'highcharts-color-0',
        title: {
            text: 'Number of Pipelines'
        }
    }, {
        className: 'highcharts-color-1',
        opposite: true,
        title: {
            text: 'Number of Datasets'
        }
    }],

    xAxis: {
    categories: ["April'19", "May'19", "June'19", "July'19"]
    },

    plotOptions: {
        column: {
            borderRadius: 5
        }
    },



    series: [{
        name: 'CONP Datasets',
        data: [6, 7, 10, 10]
    }, {
        name: 'CONP Pipelines',
        data: [0, 0, 45, 45],
        yAxis: 1
    }]

});