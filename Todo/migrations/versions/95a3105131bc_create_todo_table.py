"""Create todo table

Revision ID: 95a3105131bc
Revises: bf94a6ff17f6
Create Date: 2024-11-21 13:14:30.731783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95a3105131bc'
down_revision: Union[str, None] = 'bf94a6ff17f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
        'todos',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('priority', sa.String(), nullable=True),
        sa.Column('complete', sa.Boolean(), default=False, nullable=False),
        sa.Column('owner_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("todos")
