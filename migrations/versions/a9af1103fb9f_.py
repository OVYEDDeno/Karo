"""empty message

Revision ID: a9af1103fb9f
Revises: 2813e3bee2f7
Create Date: 2023-09-10 13:54:05.188004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9af1103fb9f'
down_revision = '2813e3bee2f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.alter_column('receiver_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['creator_id'])
        batch_op.create_unique_constraint(None, ['receiver_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('receiver_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
