from database.postgreSQL_connection import Database
from database.db_login_info import database_name, user_name, user_password, host_name
from data.data_types import Users, Heroes, Items, HeroSlots
from data.manipulate_items import CreateItems, HeroStats
from random import randint

# Initialize database connection
Database.initialise(database=database_name, user=user_name, password=user_password, host=host_name, port=5432)

USER_CHOICE = """
1. Start Adventure
2. View Inventory
3. View HeroStats
"""

slots_for_my_hero = HeroSlots('Godlike')
print(slots_for_my_hero)

slots_after_db = slots_for_my_hero._get_hero_slots_from_db()
print(slots_for_my_hero)

slots_for_my_hero._update_slots_db()

print(slots_for_my_hero)

Database.close_all_connections()

