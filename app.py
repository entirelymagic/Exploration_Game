from database.postgreSQL_connection import Database
from database.db_login_info import database_name, user_name, user_password, host_name

# Initialize database connection
Database.initialise(database=database_name, user=user_name, password=user_password, host=host_name)


