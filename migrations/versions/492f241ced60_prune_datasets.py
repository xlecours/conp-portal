"""prune_datasets

Revision ID: 492f241ced60
Revises: c4780889e90b
Create Date: 2019-11-28 12:24:58.385079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '492f241ced60'
down_revision = 'c4780889e90b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dataset_stats', schema=None) as batch_op:
        batch_op.drop_index('ix_dataset_stats_dataset_id')
        batch_op.drop_index('ix_dataset_stats_files')
        batch_op.drop_index('ix_dataset_stats_num_downloads')
        batch_op.drop_index('ix_dataset_stats_num_likes')
        batch_op.drop_index('ix_dataset_stats_num_subjects')
        batch_op.drop_index('ix_dataset_stats_num_views')
        batch_op.drop_index('ix_dataset_stats_size')
        batch_op.drop_index('ix_dataset_stats_sources')

    op.drop_table('dataset_stats')
    with op.batch_alter_table('datasets', schema=None) as batch_op:
        batch_op.drop_index('ix_datasets_annex_uuid')
        batch_op.drop_index('ix_datasets_category')
        batch_op.drop_index('ix_datasets_format')
        batch_op.drop_index('ix_datasets_modality')
        batch_op.drop_index('ix_datasets_owner_id')
        batch_op.drop_column('owner_id')
        batch_op.drop_column('image')
        batch_op.drop_column('annex_uuid')
        batch_op.drop_column('format')
        batch_op.drop_column('category')
        batch_op.drop_column('modality')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('datasets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modality', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('format', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('annex_uuid', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('image', sa.BLOB(), nullable=True))
        batch_op.add_column(sa.Column('owner_id', sa.INTEGER(), nullable=True))
        batch_op.create_index('ix_datasets_owner_id', ['owner_id'], unique=False)
        batch_op.create_index('ix_datasets_modality', ['modality'], unique=False)
        batch_op.create_index('ix_datasets_format', ['format'], unique=False)
        batch_op.create_index('ix_datasets_category', ['category'], unique=False)
        batch_op.create_index('ix_datasets_annex_uuid', ['annex_uuid'], unique=1)

    op.create_table('dataset_stats',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('dataset_id', sa.VARCHAR(length=64), nullable=True),
    sa.Column('size', sa.INTEGER(), nullable=True),
    sa.Column('files', sa.INTEGER(), nullable=True),
    sa.Column('sources', sa.INTEGER(), nullable=True),
    sa.Column('num_subjects', sa.INTEGER(), nullable=True),
    sa.Column('num_downloads', sa.INTEGER(), nullable=True),
    sa.Column('num_likes', sa.INTEGER(), nullable=True),
    sa.Column('num_views', sa.INTEGER(), nullable=True),
    sa.Column('date_updated', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('dataset_stats', schema=None) as batch_op:
        batch_op.create_index('ix_dataset_stats_sources', ['sources'], unique=False)
        batch_op.create_index('ix_dataset_stats_size', ['size'], unique=False)
        batch_op.create_index('ix_dataset_stats_num_views', ['num_views'], unique=False)
        batch_op.create_index('ix_dataset_stats_num_subjects', ['num_subjects'], unique=False)
        batch_op.create_index('ix_dataset_stats_num_likes', ['num_likes'], unique=False)
        batch_op.create_index('ix_dataset_stats_num_downloads', ['num_downloads'], unique=False)
        batch_op.create_index('ix_dataset_stats_files', ['files'], unique=False)
        batch_op.create_index('ix_dataset_stats_dataset_id', ['dataset_id'], unique=1)

    # ### end Alembic commands ###
