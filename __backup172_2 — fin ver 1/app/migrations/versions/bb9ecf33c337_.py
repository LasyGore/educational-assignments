"""empty message

Revision ID: bb9ecf33c337
Revises: 58487e5e5983
Create Date: 2024-09-03 19:38:02.771159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb9ecf33c337'
down_revision: Union[str, None] = '58487e5e5983'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
