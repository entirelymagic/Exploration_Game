from database.postgreSQL_connection import CursorFromConnectionPool
import psycopg2.extras
import uuid


class Users:
    """User class, will have email as the primary key when looking for it in the database."""
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User {}>".format(self.email)

    def create_new_user(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() as cursor:
            SQL = 'INSERT INTO users VALUES (%s, %s, %s)'
            cursor.execute(SQL, (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionPool() as cursor:
            # Note the (email,) to make it a tuple!
            sql = 'SELECT * FROM users WHERE email= %s'
            cursor.execute(sql, (email,))
            user_data = cursor.fetchone()
            return cls(email=user_data[0],
                       first_name=user_data[1],
                       last_name=user_data[2],
                       )

    @classmethod
    def _use_SQL(cls, sql):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(sql)


class Heroes:
    def __init__(self, hero_name, account, lvl=1, hp=100, attack=1, defense=1,
                 fire_attack=1, fire_res=1, stash_size=50):
        self.hero_name = hero_name
        self.lvl = lvl
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.fire_res = fire_res
        self.fire_attack = fire_attack
        self.account = account
        self.stash_size = stash_size

    def __repr__(self):
        return f"""Character <{self.hero_name}>
                lvl: {self.lvl}
                hp: {self.hp} 
                attack: {self.attack}
                defense: {self.defense}
                fire attack: {self.fire_attack}
                fire resist: {self.fire_res}
                account: {self.account}
                """

    def _create_new_character(self):
        with CursorFromConnectionPool() as cursor:
            sql = "INSERT INTO heroes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.hero_name, self.lvl, self.hp, self.attack, self.defense,
                                 self.fire_attack, self.fire_res, self.account, self.stash_size))

    @classmethod
    def load_from_db_by_char_name(cls, hero_name):
        with CursorFromConnectionPool() as cursor:
            # Note the (email,) to make it a tuple!
            sql = 'SELECT * FROM heroes WHERE hero_name= %s'
            cursor.execute(sql, (hero_name,))
            character_data = cursor.fetchone()
            return cls(hero_name=character_data[0],
                       lvl=character_data[1],
                       hp=character_data[2],
                       attack=character_data[3],
                       defense=character_data[4],
                       fire_attack=character_data[5],
                       fire_res=character_data[6],
                       account=character_data[7]
                       )

    @classmethod
    def _useSQL(cls, sql):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(sql)


class Items:
    def __init__(self, item_name, hero_name, item_type, rarity, item_lvl=1,
                 item_attack=0, item_defense=0, fire_attack=0, fire_res=0, equipped=False,):
        psycopg2.extras.register_uuid()
        self.item_id = uuid.uuid4()
        self.item_name = item_name
        self.hero_name = hero_name
        self.item_type = item_type
        self.rarity = rarity
        self.item_lvl = item_lvl
        self.item_attack = item_attack
        self.item_defense = item_defense
        self.fire_attack = fire_attack
        self.fire_res = fire_res
        self.equipped = equipped

    ITEM_RARITY = {
        0: 'Normal',
        1: 'Rare',
        2: 'Mythical',
        3: 'Legendary'
    }

    ITEM_TYPE = {

    }

    def __repr__(self):
        return f"""Character <{self.hero_name}>
                item_id {self.item_id}
                item_name: {self.item_name}
                item_lvl: {self.item_lvl} 
                item_type: {self.item_type}
                rarity: {self.ITEM_RARITY[self.rarity]}
                fire attack: {self.fire_attack}
                fire resist: {self.fire_res}
                attack: {self.item_attack}
                defense: {self.item_defense}
                equipped: {self.equipped}
                """

    def create_new_item(self):
        with CursorFromConnectionPool() as cursor:
            sql = "INSERT INTO items VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.item_id,
                                 self.item_name,
                                 self.hero_name,
                                 self.item_type,
                                 self.rarity,
                                 self.equipped,
                                 self.item_attack,
                                 self.item_defense,
                                 self.fire_attack,
                                 self.fire_res,
                                 self.item_lvl)
                           )
    @classmethod
    def load_item_from_db_by_hero_name(cls, hero_name):
        with CursorFromConnectionPool() as cursor:
            sql = 'SELECT * FROM items WHERE character_name = %s'
            cursor.execute(sql, (hero_name,))
            character_data = cursor.fetchall()
            return character_data

    def useSQL(self, sql):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(sql)


class Monsters:
    def __init__(self, name, lvl, hp, attack, defense):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def create_new_monster(self):
        with CursorFromConnectionPool() as cursor:
            sql = "INSERT into monsters VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.name, self.lvl,
                                 self.hp, self.attack, self.defense)
                           )
