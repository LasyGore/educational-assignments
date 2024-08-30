"""empty message

Revision ID: 3c3f6b88ccdf
Revises: 4875e3fb9e9e
Create Date: 2024-08-30 01:41:07.521283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c3f6b88ccdf'
down_revision: Union[str, None] = '4875e3fb9e9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
