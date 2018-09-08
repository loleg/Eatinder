"""empty message

Revision ID: ae95307a98a3
Revises: 
Create Date: 2018-09-08 19:11:26.187393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae95307a98a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('label',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=64), nullable=False),
    sa.Column('of_type', sa.Enum('Food Preferences', 'Dietary Requirements', 'Environmental Impact', name='Type'), nullable=False),
    sa.Column('icon', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=256), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('label_meal',
    sa.Column('label_id', sa.Integer(), nullable=True),
    sa.Column('meal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['label_id'], ['label.id'], ),
    sa.ForeignKeyConstraint(['meal_id'], ['meal.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('label_meal')
    op.drop_table('meal')
    op.drop_table('label')
    # ### end Alembic commands ###