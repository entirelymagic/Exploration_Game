from data.fighting import Fighting
from database.postgreSQL_connection import Database
from database.db_login_info import database_name, user_name, user_password, host_name
from data.data_types import Users, Heroes, Items, HeroSlots
from data.manipulate_items import CreateItems, HeroStats, CreateMonster
from random import randint

# Initialize database connection
Database.initialise(database=database_name,
                    user=user_name,
                    password=user_password,
                    host=host_name,
                    port=5432)

USER_CHOICE = """
1. Start Adventure
2. View Inventory
3. View HeroStats
"""
my_hero = HeroStats('Godlike', 'elvis.munteanu@gmail.com')

print(my_hero.hero_slots)
print(my_hero)
my_hero.update_slots_db()

monster1 = CreateMonster(1)
print(monster1)
fight = Fighting(my_hero, monster1)
winner = fight.winner
print(winner)
print(my_hero)
Database.close_all_connections()


