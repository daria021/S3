"""delete user_file

Revision ID: 25e9e63b051a
Revises: 0af86c5951f6
Create Date: 2024-07-21 22:58:31.646512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25e9e63b051a'
down_revision: Union[str, None] = '0af86c5951f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_file')
    op.add_column('file', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'file', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'file', type_='foreignkey')
    op.drop_column('file', 'user_id')
    op.create_table('user_file',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('file_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], name='user_file_file_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_file_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='user_file_pkey')
    )
    # ### end Alembic commands ###
