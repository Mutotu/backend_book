"""add-columns-to-user

Revision ID: f9ef1f69a095
Revises: c89215bf8bf5
Create Date: 2022-01-08 16:11:07.451880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9ef1f69a095'
down_revision = 'c89215bf8bf5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("bike_post", sa.Column("user_id",sa.Integer))


def downgrade():
    op.remove_column("bike_post", "user_id")
