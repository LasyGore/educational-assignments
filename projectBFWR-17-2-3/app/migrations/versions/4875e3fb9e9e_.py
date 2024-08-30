"""empty message

Revision ID: 4875e3fb9e9e
Revises: 0ff667ae9518
Create Date: 2024-08-30 01:38:41.026730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4875e3fb9e9e'
down_revision: Union[str, None] = '0ff667ae9518'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
