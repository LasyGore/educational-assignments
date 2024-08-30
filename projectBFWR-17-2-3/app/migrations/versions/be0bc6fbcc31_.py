"""empty message

Revision ID: be0bc6fbcc31
Revises: 1b4024910ea2
Create Date: 2024-08-30 00:11:50.726117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be0bc6fbcc31'
down_revision: Union[str, None] = '1b4024910ea2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
