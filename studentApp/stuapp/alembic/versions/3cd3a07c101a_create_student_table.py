"""create student table

Revision ID: 3cd3a07c101a
Revises: 
Create Date: 2021-06-14 11:41:41.392611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cd3a07c101a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'students',
        sa.Column('stuId', sa.String(50), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
        
    )


def downgrade():
    pass
