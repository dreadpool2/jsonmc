"""empty message

Revision ID: 6415c74704d9
Revises: ec7d4c35740b
Create Date: 2016-07-24 08:23:40.300208

"""

# revision identifiers, used by Alembic.
revision = '6415c74704d9'
down_revision = 'ec7d4c35740b'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('type', sa.String(), nullable=True))
    op.alter_column('ticket', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('ticket', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('ticket', 'sales_end',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('ticket', 'sales_start',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ticket', 'sales_start',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('ticket', 'sales_end',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('ticket', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('ticket', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('ticket', 'type')
    ### end Alembic commands ###
