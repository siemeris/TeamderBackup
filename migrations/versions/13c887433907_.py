"""empty message

Revision ID: 13c887433907
Revises: a40e66eab4f2
Create Date: 2022-08-19 19:00:43.503527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13c887433907'
down_revision = 'a40e66eab4f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('activities_user_id_fkey', 'activities', type_='foreignkey')
    op.drop_column('activities', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activities', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('activities_user_id_fkey', 'activities', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
