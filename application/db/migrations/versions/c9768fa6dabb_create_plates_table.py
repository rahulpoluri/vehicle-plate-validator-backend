"""create plates table

Revision ID: c9768fa6dabb
Revises:
Create Date: 2024-12-25 00:11:34.303348

"""

import os
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from passlib.hash import pbkdf2_sha256  # type: ignore

SUPER_ADMIN_USER_NAME = os.getenv("SUPER_ADMIN_USER_NAME")
SUPER_ADMIN_PASSWORD = os.getenv("SUPER_ADMIN_PASSWORD")

# revision identifiers, used by Alembic.
revision: str = "c9768fa6dabb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

if not SUPER_ADMIN_USER_NAME or not SUPER_ADMIN_PASSWORD:
    raise ValueError(
        "Environment variables SUPER_ADMIN_USER_NAME and "
        "SUPER_ADMIN_PASSWORD must be set."
    )


def upgrade() -> None:
    op.create_table(
        "plates",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("plate", sa.String(20), nullable=False),
        sa.Column(
            "timestamp",
            sa.TIMESTAMP,
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    users_table = op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(50), nullable=False),
        sa.Column("password", sa.String(255), nullable=False),
        sa.Column("role", sa.String(20), nullable=False),
    )

    op.bulk_insert(
        users_table,
        [
            {
                "username": SUPER_ADMIN_USER_NAME,
                "password": pbkdf2_sha256.hash(SUPER_ADMIN_PASSWORD),
                "role": "superadmin",
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("plates")
    op.drop_table("users")
