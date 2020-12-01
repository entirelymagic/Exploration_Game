from database.postgreSQL_connection import Database
from database.db_login_info import database_name, user_name, user_password, host_name
from data.data_types import Users, Heroes, Items

# Initialize database connection
Database.initialise(database=database_name, user=user_name, password=user_password, host=host_name, port=5432)


first_char = Heroes('Godlike', 'elvis.munteanu@gmail.com')
wood_helmet = Items('Wood helmet', first_char.hero_name, 'helmet', 0)
wood_helmet.create_new_item()
first_char.load_from_db_by_char_name(first_char.hero_name)
print(first_char)
items = Items.load_item_from_db_by_hero_name(first_char.hero_name)
print(items)


Database.close_all_connections()
#
