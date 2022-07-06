"""Initial migration

Revision ID: d0c0721c294b
Revises: 
Create Date: 2022-07-05 10:57:12.260816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0c0721c294b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rates_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('usd_rate', sa.Float(), nullable=True),
    sa.Column('eur_rate', sa.Float(), nullable=True),
    sa.Column('chd_rate', sa.Float(), nullable=True),
    sa.Column('jpy_rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rates_table')
    # ### end Alembic commands ###
