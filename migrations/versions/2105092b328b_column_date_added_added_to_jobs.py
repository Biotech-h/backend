"""Column_date-added_added_to_jobs

Revision ID: 2105092b328b
Revises: 6fdd7b573369
Create Date: 2022-09-12 23:54:23.012845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2105092b328b'
down_revision = 'ac91ecdd3317'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('date_added', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jobs', 'date_added')
    # ### end Alembic commands ###
