"""merging two heads

Revision ID: 820b5eb59ba9
Revises: dfb7b89656ae, 2bd795c13a09, 40c4a42a5c56, 807d53c63db0
Create Date: 2022-02-05 22:39:33.223954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '820b5eb59ba9'
down_revision = ('dfb7b89656ae', '2bd795c13a09', '40c4a42a5c56', '807d53c63db0')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
