"""empty message

Revision ID: 87ce13b7a378
Revises: 
Create Date: 2023-09-10 13:27:32.115534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87ce13b7a378'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('wager', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('creator_move1', sa.Enum('Rock', 'Paper', 'Scissor', name='movetypes'), nullable=False),
    sa.Column('creator_move2', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('creator_move3', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('creator_move4', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('creator_move5', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('receiver_move1', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('receiver_move2', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('receiver_move3', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('receiver_move4', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('receiver_move5', sa.Enum(name='movetypes'), nullable=False),
    sa.Column('result', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('category', sa.Boolean(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request')
    op.drop_table('game')
    op.drop_table('user')
    # ### end Alembic commands ###