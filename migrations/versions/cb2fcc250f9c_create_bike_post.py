"""create_bike_post

Revision ID: cb2fcc250f9c
Revises: cd64adf82450
Create Date: 2022-01-07 19:50:30.538555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb2fcc250f9c'
down_revision = 'cd64adf82450'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'bike_post',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('photo', sa.String, nullable=False),
        sa.Column('make', sa.String, nullable=False),
        sa.Column('model', sa.String, nullable=False),
        sa.Column('year',sa.String, nullable=False),
        sa.Column('price',sa.String, nullable=False),
        sa.Column('availability',sa.String, nullable=False),
        sa.Column('comments',sa.String), 
        
    )


def downgrade():
    op.drop_table('bike_post')
