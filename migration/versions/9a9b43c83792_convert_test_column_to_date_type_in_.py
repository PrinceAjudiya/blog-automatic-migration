"""Convert test column to date type in comment table

Revision ID: 9a9b43c83792
Revises: 8a84fbf06146
Create Date: 2024-05-26 14:41:18.317311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9a9b43c83792'
down_revision: Union[str, None] = '8a84fbf06146'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('new_time', sa.TIMESTAMP(timezone=True)))
    op.execute("""
        UPDATE category
        SET new_time = to_timestamp(time)
    """)
    op.drop_column('category', 'time')
    op.alter_column('category', 'new_time', new_column_name='time')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TABLE category ALTER COLUMN time TYPE FLOAT USING EXTRACT(EPOCH FROM time)::FLOAT")
    # ### end Alembic commands ###
