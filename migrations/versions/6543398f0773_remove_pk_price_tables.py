"""remove pk price tables

Revision ID: 6543398f0773
Revises: f5518fbefd44
Create Date: 2016-02-17 19:54:47.359000

"""

# revision identifiers, used by Alembic.
revision = '6543398f0773'
down_revision = 'f5518fbefd44'

import sqlalchemy as sa

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'item_adjusted_price_ibfk_1', 'item_adjusted_price', type_='foreignkey')
    op.drop_constraint(u'item_price_ibfk_1', 'item_price', type_='foreignkey')
    op.drop_constraint(u'item_price_ibfk_2', 'item_price', type_='foreignkey')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
