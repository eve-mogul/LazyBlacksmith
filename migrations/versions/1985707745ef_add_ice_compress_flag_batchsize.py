"""add ice compress flag batchsize

Revision ID: 1985707745ef
Revises: d7ae554d1766
Create Date: 2016-09-01 10:55:11.131417

"""

# revision identifiers, used by Alembic.
revision = '1985707745ef'
down_revision = 'd7ae554d1766'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ore_refining', sa.Column('batch', sa.Integer(), nullable=True))
    op.add_column('ore_refining', sa.Column('is_compressed', sa.Boolean(), nullable=True))
    op.add_column('ore_refining', sa.Column('is_ice', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ore_refining', 'is_ice')
    op.drop_column('ore_refining', 'is_compressed')
    op.drop_column('ore_refining', 'batch')
    ### end Alembic commands ###