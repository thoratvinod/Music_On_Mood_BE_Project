"""Adding Playlist

Revision ID: 37b9c401cfa2
Revises: 14e456fcf9ea
Create Date: 2020-03-20 17:38:10.237210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37b9c401cfa2'
down_revision = '14e456fcf9ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playlist',
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.Column('playlist_title', sa.String(length=200), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('emotion', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('playlist_id')
    )
    op.create_table('track_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Playlist_id', sa.Integer(), nullable=False),
    sa.Column('Track_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('track', sa.Column('playlist', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('track', 'playlist')
    op.drop_table('track_group')
    op.drop_table('playlist')
    # ### end Alembic commands ###
