"""empty message

Revision ID: 2813e3bee2f7
Revises: 87ce13b7a378
Create Date: 2023-09-10 13:47:05.319429

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2813e3bee2f7'
down_revision = '87ce13b7a378'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request')
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.alter_column('creator_move1',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('creator_move2',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('creator_move3',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('creator_move4',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('creator_move5',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('receiver_move1',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('receiver_move2',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('receiver_move3',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('receiver_move4',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)
        batch_op.alter_column('receiver_move5',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.alter_column('receiver_move5',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('receiver_move4',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('receiver_move3',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('receiver_move2',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('receiver_move1',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('creator_move5',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('creator_move4',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('creator_move3',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('creator_move2',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)
        batch_op.alter_column('creator_move1',
               existing_type=postgresql.ENUM('Rock', 'Paper', 'Scissor', name='movetypes'),
               nullable=False)

    op.create_table('request',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('creator_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('receiver_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('category', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], name='request_creator_id_fkey'),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], name='request_receiver_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='request_pkey')
    )
    # ### end Alembic commands ###
