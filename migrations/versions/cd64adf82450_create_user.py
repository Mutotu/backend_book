"""create_user

Revision ID: cd64adf82450
Revises: 
Create Date: 2022-01-07 19:50:08.002792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd64adf82450'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False, unique=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String,nullable=False),
        
    )


def downgrade():
    op.drop_table('user')


# alembic revision add-columns-to-user