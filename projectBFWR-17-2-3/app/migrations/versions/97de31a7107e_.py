"""empty message

Revision ID: 97de31a7107e
Revises: 3c3f6b88ccdf
Create Date: 2024-08-30 08:42:09.307859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97de31a7107e'
down_revision: Union[str, None] = '3c3f6b88ccdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
