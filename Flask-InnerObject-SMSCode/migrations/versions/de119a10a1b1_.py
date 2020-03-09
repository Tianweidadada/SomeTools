"""empty message

Revision ID: de119a10a1b1
Revises: 3ceeda8f09a9
Create Date: 2020-03-08 18:14:45.357335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de119a10a1b1'
down_revision = '3ceeda8f09a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('s_phone', sa.String(length=32), nullable=True))
    op.create_unique_constraint(None, 'student', ['s_phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='unique')
    op.drop_column('student', 's_phone')
    # ### end Alembic commands ###
