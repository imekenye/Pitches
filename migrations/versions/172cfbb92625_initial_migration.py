"""Initial Migration

Revision ID: 172cfbb92625
Revises: 56bed9e3ac50
Create Date: 2019-04-22 10:49:39.907127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '172cfbb92625'
down_revision = '56bed9e3ac50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('feedback', sa.String(length=1000), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
