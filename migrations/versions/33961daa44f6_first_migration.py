"""first migration

Revision ID: 33961daa44f6
Revises: 
Create Date: 2022-09-07 23:08:57.627977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33961daa44f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pi_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('param_name', sa.String(length=8), nullable=False),
    sa.Column('pretty_name', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('param_name')
    )
    op.create_table('pi_vendor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('param_name', sa.String(length=16), nullable=False),
    sa.Column('pretty_name', sa.String(length=32), nullable=False),
    sa.Column('country', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('param_name')
    )
    op.create_table('workspace',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slack_id', sa.String(length=16), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('bot_token', sa.String(length=64), nullable=False),
    sa.Column('bot_user_id', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slack_id')
    )
    op.create_table('subscriber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slack_id', sa.String(length=16), nullable=False),
    sa.Column('workspace', sa.Integer(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['workspace'], ['workspace.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pi_subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subscriber', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subscriber'], ['subscriber.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pi_subscription_to_type',
    sa.Column('subscription_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subscription_id'], ['pi_subscription.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['pi_type.id'], )
    )
    op.create_table('pi_subscription_to_vendor',
    sa.Column('subscription_id', sa.Integer(), nullable=True),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subscription_id'], ['pi_subscription.id'], ),
    sa.ForeignKeyConstraint(['vendor_id'], ['pi_vendor.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pi_subscription_to_vendor')
    op.drop_table('pi_subscription_to_type')
    op.drop_table('pi_subscription')
    op.drop_table('subscriber')
    op.drop_table('workspace')
    op.drop_table('pi_vendor')
    op.drop_table('pi_type')
    # ### end Alembic commands ###
