"""enable pgvector extension

Base migration: enables the pgvector extension. New migrations chain off it.

Revision ID: c3e7f1a2b4d6
Revises: (base)
Create Date: 2026-06-16

"""

from alembic import op

revision = "c3e7f1a2b4d6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector;")


def downgrade() -> None:
    op.execute("DROP EXTENSION IF EXISTS vector;")
