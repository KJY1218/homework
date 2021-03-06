"""empty message

Revision ID: 1d781c8eca0d
Revises: 2640b5a24351
Create Date: 2014-08-06 19:57:50.449000

"""

# revision identifiers, used by Alembic.
revision = '1d781c8eca0d'
down_revision = '2640b5a24351'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('author', sa.String(length=255), nullable=True))
    op.add_column('article', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('article', sa.Column('date_created', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'date_created')
    op.drop_column('article', 'category')
    op.drop_column('article', 'author')
    ### end Alembic commands ###
