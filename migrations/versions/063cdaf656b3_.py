"""empty message

Revision ID: 063cdaf656b3
Revises: 2e5d9ec3340f
Create Date: 2019-04-28 15:05:03.568687

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '063cdaf656b3'
down_revision = '2e5d9ec3340f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dataset_stats', 'date_updated',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('datasets', 'date_created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('datasets', 'date_updated',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('datasets', 'date_updated',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('datasets', 'date_created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('dataset_stats', 'date_updated',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###