"""empty message

Revision ID: ad7f50c4afb5
Revises: 9913b58c2640
Create Date: 2016-07-29 23:33:03.981000

"""

# revision identifiers, used by Alembic.
revision = 'ad7f50c4afb5'
down_revision = '9913b58c2640'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('status', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'status')
    ### end Alembic commands ###
