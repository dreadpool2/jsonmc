"""empty message

Revision ID: 217d3c1f3c5f
Revises: ccd80550c01f
Create Date: 2017-06-12 03:24:22.545460

"""

# revision identifiers, used by Alembic.
revision = '217d3c1f3c5f'
down_revision = 'ccd80550c01f'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('notification', 'notifications')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('notifications', 'notification')
    # ### end Alembic commands ###
