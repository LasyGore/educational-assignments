"""empty message

Revision ID: 0ff667ae9518
Revises: be0bc6fbcc31
Create Date: 2024-08-30 01:31:30.159764

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ff667ae9518'
down_revision: Union[str, None] = 'be0bc6fbcc31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
