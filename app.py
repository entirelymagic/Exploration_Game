from database.postgreSQL_connection import Database
from database.db_login_info import database_name, user_name, user_password, host_name
from data.data_types import Users, Heroes, Items
from data.manipulate_items import CreateItems, HeroStats
from random import randint

# Initialize database connection
Database.initialise(database=database_name, user=user_name, password=user_password, host=host_name, port=5432)

USER_CHOICE = """

"""

this_hero = HeroStats.load_from_db_by_char_name('Godlike')
print(this_hero)
Database.close_all_connections()

