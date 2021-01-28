from itertools import islice

from postgreSQL_connection import CursorFromConnectionPool
from src.user import User, Hero, Item


def _add_user_to_db(user):
    # This is creating a new connection pool every time! Very expensive...
    """Add a new user to the database when it is created."""

    with CursorFromConnectionPool() as cursor:
        SQL = 'INSERT INTO users VALUES (%s, %s, %s, %s)'
        cursor.execute(SQL, (user.email, user.first_name, user.last_name, user.heroes))


def _load_user_from_db_by_email(email):
    """Load User information from DB and return a User object"""

    with CursorFromConnectionPool() as cursor:
        # Note the (email,) to make it a tuple!
        sql = 'SELECT * FROM users WHERE email= %s'
        cursor.execute(sql, (email,))
        user_data = cursor.fetchone()
        return User(
            email=user_data[0],
            first_name=user_data[1],
            last_name=user_data[2],
            heroes=list(user_data[3]),
        )


def _use_SQL(sql, *args):
    """Execute a database statement, just for testing, will be removed after."""

    with CursorFromConnectionPool() as cursor:
        cursor.execute(sql, (*args,))


def _add_new_hero_to_db(hero):
    """Add a new hero to the database"""

    with CursorFromConnectionPool() as cursor:
        sql = "INSERT INTO heroes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (hero.hero_name, hero.lvl, hero.hp, hero.attack, hero.defense,
                             hero.fire_attack, hero.fire_res, hero.account, hero.stash_size))


def load_hero_from_db_by_name(hero_name):
    """Providing the hero name, connect to DB and create a Hero Object with values from DB"""

    with CursorFromConnectionPool() as cursor:
        # Note the (email,) to make it a tuple!
        sql = 'SELECT * FROM heroes WHERE hero_name= %s'
        cursor.execute(sql, (hero_name,))
        hero_data = cursor.fetchone()

        return Hero(
            hero_name=hero_data[0],
            account=hero_data[1],
            stash_size=hero_data[2],
            lvl=hero_data[3],
            hp=hero_data[4],
            attack=hero_data[5],
            defense=hero_data[6],
            hero_slots=hero_data[7],
            inventory=hero_data[8],
            current_hp=hero_data[9],
        )


def add_new_item_to_db(item):
    """Add a new item to database"""

    with CursorFromConnectionPool() as cursor:
        sql = "INSERT INTO items VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
            item.item_id,
            item.item_name,
            item.hero_name,
            item.item_type,
            item.rarity,
            item.equipped,
            item.item_attack,
            item.item_defense,
            item.fire_attack,
            item.fire_res,
            item.item_lvl)
                       )


def load_items_from_db_by_hero_name(hero_name):
    """Retrieve items related to the hero name provided."""

    with CursorFromConnectionPool() as cursor:
        sql = 'SELECT * FROM items WHERE hero_name = %s'
        cursor.execute(sql, (hero_name,))
        character_data = cursor.fetchall()
        return [list(item) for item in character_data]


def update_item_equipped_status_to_database(id_item, status):
    with CursorFromConnectionPool() as cursor:
        sql = 'UPDATE items SET equipped = %s WHERE item_id = %s'
        cursor.execute(sql, (status, id_item))


def add_new_monster_to_db(monster):
    with CursorFromConnectionPool() as cursor:
        sql = "INSERT into monsters VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
            monster.name,
            monster.lvl,
            monster.hp,
            monster.attack,
            monster.defense,
            monster.xp,
        ))


def get_hero_slots_from_db(item):
    with CursorFromConnectionPool() as cursor:
        sql = "SELECT * FROM hero_slots WHERE hero_name = %s"
        cursor.execute(sql, (item.hero_name,))
        item.hero_slots.update(
            zip(item.hero_slots, islice(cursor.fetchone(), 1, None))
        )


def update_slots_db(hero):
    with CursorFromConnectionPool() as cursor:
        sql = (
                "UPDATE hero_slots SET " +
                ", ".join(f"{slot.lower()} = %s" for slot in hero.hero_slots) +
                " WHERE hero_name = %s"
        )

        cursor.execute(sql, (*hero.hero_slots.values(), hero.hero_name))


def _create_slots_db(hero_slots):
    with CursorFromConnectionPool() as cursor:
        sql = 'INSERT into hero_slots VALUES(' \
              '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, (
            hero_slots.hero_name,
            *hero_slots.hero_slots.values()
        ))
