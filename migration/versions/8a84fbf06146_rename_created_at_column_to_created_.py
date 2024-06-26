"""Rename created_at column to created_date in comment table

Revision ID: 8a84fbf06146
Revises: 0bd9c1abeebe
Create Date: 2024-05-26 12:45:42.898267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a84fbf06146'
down_revision: Union[str, None] = '0bd9c1abeebe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'created_at', new_column_name='created_date', existing_type=sa.DateTime(), existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'created_date', new_column_name='created_at', existing_type=sa.DateTime(), existing_nullable=True)
    # ### end Alembic commands ###
