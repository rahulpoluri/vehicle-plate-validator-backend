"""create plates table

Revision ID: c9768fa6dabb
Revises:
Create Date: 2024-12-25 00:11:34.303348

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c9768fa6dabb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "plates",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("plate", sa.String(20), nullable=False),
        sa.Column("timestamp", sa.TIMESTAMP, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("plates")
