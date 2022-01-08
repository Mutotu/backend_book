"""create_bikes_saved

Revision ID: c89215bf8bf5
Revises: cb2fcc250f9c
Create Date: 2022-01-07 19:50:37.749127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c89215bf8bf5'
down_revision = 'cb2fcc250f9c'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'bikes_saved',
         sa.Column('id',sa.Integer, primary_key=True),
         sa.Column('user_id', sa.Integer),
         sa.Column('bike_pos_id', sa.Integer)
    )


def downgrade():
    op.drop_table('bikes_saved')
