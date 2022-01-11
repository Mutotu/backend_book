"""add-columns-to-user

Revision ID: 660cdfb323b9
Revises: f9ef1f69a095
Create Date: 2022-01-08 19:12:53.262645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '660cdfb323b9'
down_revision = 'f9ef1f69a095'
branch_labels = None
depends_on = None


# def upgrade():
#     op.add_column('user', sa.Column('id', sa.Integer, primary_key=True))
#     op.add_column('user', sa.Column('username', sa.String,nullable=False, unique=True ))
#     op.add_column('user', sa.Column('email', sa.String, nullable=False, unique=True))
#     op.add_column('user', sa.Column('password', sa.String))
# def downgrade():
#     op.remove_column('user', 'id')
#     op.remove_column('user', 'username')
#     op.remove_column('user', 'email')
#     op.remove_column('user', 'password')
