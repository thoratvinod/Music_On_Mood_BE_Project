"""adding table again

Revision ID: e9709bd9ecb7
Revises: bb56c8e3484d
Create Date: 2020-03-20 20:07:06.281453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9709bd9ecb7'
down_revision = 'bb56c8e3484d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('track_group', sa.Column('pl_id', sa.Integer(), nullable=False))
    op.add_column('track_group', sa.Column('tg_id', sa.Integer(), nullable=False))
    op.add_column('track_group', sa.Column('track_id', sa.Integer(), nullable=False))
    op.drop_column('track_group', 'Playlist_id')
    op.drop_column('track_group', 'id')
    op.drop_column('track_group', 'Track_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('track_group', sa.Column('Track_id', sa.INTEGER(), nullable=False))
    op.add_column('track_group', sa.Column('id', sa.INTEGER(), nullable=False))
    op.add_column('track_group', sa.Column('Playlist_id', sa.INTEGER(), nullable=False))
    op.drop_column('track_group', 'track_id')
    op.drop_column('track_group', 'tg_id')
    op.drop_column('track_group', 'pl_id')
    # ### end Alembic commands ###
