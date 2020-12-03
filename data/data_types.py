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
    def _use_SQL(cls, sql, *args):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(sql, (*args,))


class Heroes:
    def __init__(self, hero_name, account, lvl=1, hp=500, attack=10, defense=10,
                 fire_attack=0, fire_res=0, stash_size=50):
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
    def _use_SQL(cls, sql, *args):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(sql, (*args,))


class Items:
    """Used to connect and get from the PostgresQl database."""
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
            return [list(item) for item in character_data]

    @classmethod
    def update_item_status(cls, id_item, status):
        with CursorFromConnectionPool() as cursor:
            sql = 'UPDATE items SET equipped = %s WHERE item_id = %s'
            cursor.execute(sql, (status, id_item))

    @classmethod
    def _use_SQL(cls, sql, *args):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(sql, (*args,))


class Monsters:
    """Not Implemented Yet!"""
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


class HeroSlots:
    def __init__(self, hero_name):
        self.hero_name = hero_name

    hero_slots = {
        'Helmet': 0,
        'Chest': 0,
        'Belt': 0,
        'Pants': 0,
        'Boots': 0,
        'Arms': 0,
        'Left_ring': 0,
        'Right_ring': 0,
        'Amulet': 0,
        'Left_arm': 0,
        'Right_arm': 0,
    }

    def __repr__(self):
        return f"""
        {self.hero_slots}
        """

    def get_hero_slots_from_db(self):
        with CursorFromConnectionPool() as cursor:
            sql = "SELECT * FROM hero_slots WHERE hero_name = %s"
            cursor.execute(sql, (self.hero_name,))
            slots_data = list(cursor.fetchall())[0]
            slot_names = list(self.hero_slots.keys())
            self.hero_slots.update(zip(slot_names, slots_data[1:]))

    def update_slots_db(self):
        with CursorFromConnectionPool() as cursor:
            sql = 'UPDATE hero_slots SET ' \
                  'helmet = %s, ' \
                  'chest = %s, ' \
                  'belt = %s, ' \
                  'pants = %s, ' \
                  'boots = %s, ' \
                  'arms = %s, ' \
                  'left_ring = %s, ' \
                  'right_ring = %s, ' \
                  'amulet = %s, ' \
                  'left_arm = %s, ' \
                  'right_arm = %s ' \
                  ' WHERE hero_name = %s'
            cursor.execute(sql, (
                self.hero_slots['Helmet'],
                self.hero_slots['Chest'],
                self.hero_slots['Belt'],
                self.hero_slots['Pants'],
                self.hero_slots['Boots'],
                self.hero_slots['Arms'],
                self.hero_slots['Left_ring'],
                self.hero_slots['Right_ring'],
                self.hero_slots['Amulet'],
                self.hero_slots['Left_arm'],
                self.hero_slots['Right_arm'],
                self.hero_name
            ))

    def _create_slots_db(self):
        with CursorFromConnectionPool() as cursor:
            sql = 'INSERT into hero_slots VALUES(' \
                  '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (
                self.hero_name,
                self.hero_slots['helmet'],
                self.hero_slots['chest'],
                self.hero_slots['belt'],
                self.hero_slots['pants'],
                self.hero_slots['boots'],
                self.hero_slots['arms'],
                self.hero_slots['left_ring'],
                self.hero_slots['right_ring'],
                self.hero_slots['amulet'],
                self.hero_slots['left_arm'],
                self.hero_slots['right_arm']
            ))

    @classmethod
    def _use_SQL(cls, sql, *args):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(sql, (*args,))

