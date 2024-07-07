"""Create initial schema without duplicate columns

Revision ID: 01bda385a88d
Revises: 5d47a0ea1a6f
Create Date: 2024-07-07 09:19:40.245724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01bda385a88d'
down_revision = '5d47a0ea1a6f'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('restaurant_pizzas') as batch_op:
        batch_op.create_foreign_key('fk_restaurant_pizzas_pizza_id', 'pizzas', ['pizza_id'], ['id'])
        batch_op.create_foreign_key('fk_restaurant_pizzas_restaurant_id', 'restaurants', ['restaurant_id'], ['id'])


def downgrade():
    with op.batch_alter_table('restaurant_pizzas') as batch_op:
        batch_op.drop_constraint('fk_restaurant_pizzas_restaurant_id', type_='foreignkey')
        batch_op.drop_constraint('fk_restaurant_pizzas_pizza_id', type_='foreignkey')
