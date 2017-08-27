"""empty message

Revision ID: 6116f1e6c91b
Revises: 094b3006369b
Create Date: 2017-08-27 10:38:19.287742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6116f1e6c91b'
down_revision = '094b3006369b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('host', sa.Column('closeduser', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('host', 'closeduser')
    # ### end Alembic commands ###