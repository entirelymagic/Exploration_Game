from database.postgreSQL_connection import Database
from database.db_login_info import database_name, user_name, user_password, host_name
from data.data_types import Users, Heroes, Items
from data.manipulate_items import CreateItems
from random import randint

# Initialize database connection
Database.initialise(database=database_name, user=user_name, password=user_password, host=host_name, port=5432)


random_drop = CreateItems(3, randint(0, 1))
# random_drop.add_to_db('Godlike')

Database.close_all_connections()

