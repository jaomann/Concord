"""empty message

Revision ID: 4add5bfd4d8b
Revises: efb399a0d7a3
Create Date: 2023-05-09 22:02:39.694020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4add5bfd4d8b'
down_revision = 'efb399a0d7a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha_hash', sa.String(length=64), nullable=True))
        batch_op.drop_column('senha')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.VARCHAR(length=64), nullable=True))
        batch_op.drop_column('senha_hash')

    # ### end Alembic commands ###
