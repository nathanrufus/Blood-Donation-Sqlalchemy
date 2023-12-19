"""Added Blood and Contact table

Revision ID: fe97f3527a48
Revises: 7708ec448833
Create Date: 2023-12-19 17:45:50.769009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe97f3527a48'
down_revision: Union[str, None] = '7708ec448833'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Blood',
    sa.Column('B_code', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('D_id', sa.Integer(), nullable=True),
    sa.Column('B_group', sa.String(length=100), nullable=False),
    sa.Column('Packets', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['B_group'], ['BloodBank.B_group'], name=op.f('fk_Blood_B_group_BloodBank')),
    sa.ForeignKeyConstraint(['D_id'], ['Donor.D_id'], name=op.f('fk_Blood_D_id_Donor')),
    sa.PrimaryKeyConstraint('B_code')
    )
    op.create_table('Contact',
    sa.Column('Contact_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('B_group', sa.String(length=100), nullable=False),
    sa.Column('F_name', sa.String(length=100), nullable=False),
    sa.Column('C_packets', sa.Integer(), nullable=True),
    sa.Column('Adress', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['B_group'], ['BloodBank.B_group'], name=op.f('fk_Contact_B_group_BloodBank')),
    sa.PrimaryKeyConstraint('Contact_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Contact')
    op.drop_table('Blood')
    # ### end Alembic commands ###
