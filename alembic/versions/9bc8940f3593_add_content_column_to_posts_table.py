"""add content column to posts table

Revision ID: 9bc8940f3593
Revises: 9983b6940b02
Create Date: 2025-04-09 12:07:18.754400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bc8940f3593'
down_revision: Union[str, None] = '9983b6940b02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
