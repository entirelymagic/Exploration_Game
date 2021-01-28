import psycopg2.extras
import uuid

from database.eg_database_manipulation import (
    load_items_from_db_by_hero_name,
    update_item_equipped_status_to_database,
    get_hero_slots_from_db,
    update_slots_db,
)



class Hero:
    """Get the hero statistics"""
    def __init__(self, hero_name, account):
        self.hero_name = hero_name
        self.account = account
        self.stash_size = 50
        self.lvl = 1
        self.hp = self.__set_default_hp()
        self.attack = self.__set_default_attack()
        self.defense = self.__set_default_defence()
        self.hero_slots = self._get_slots()
        self.inventory = self.__get_hero_items()
        self._get_status_for_equipped_items()
        self.currentHP = self.hp
        self.hero_slots = {
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
        return f"""Character <{self.hero_name}>
                lvl: {self.lvl}
                hp: {self.currentHP}
                max_HP: {self.hp}
                attack: {self.attack}
                defense: {self.defense}
                account: {self.account}
                items: {[item.item_name for item in self.inventory]}
                """

    def _set_item_active(self, item_id):

        for item in self.inventory:
            if item[0] == item_id:
                if not item[5]:
                    item[5] = True
                    self.hero_slots[item[3]] = 1

    def __get_hero_items(self):
        self.inventory = load_items_from_db_by_hero_name(self.hero_name)
        return self.inventory

    def set_item__status_to_equipped(self, item, slot):
        item[5] = True
        self.hero_slots[slot] = 1
        update_slots_db(self)
        update_item_equipped_status_to_database(item[0], True)

    def _get_status_for_equipped_items(self):
        slots = self.hero_slots.keys()
        for item in self.inventory:
            if item[5]:
                if item[3] in slots:
                    self.__get_status_from_item(item[6], item[7])
                elif item[3] == 'One hand weapon':
                    self.__get_status_from_item(item[6], item[7])
                elif item[3] == 'Ring':
                    self.__get_status_from_item(item[6], item[7])
                elif item[3] == 'Two handed weapon':
                    self.__get_status_from_item(item[6]*3, item[7])
                elif item[3] == 'Shield':
                    self.__get_status_from_item(item[6], item[7]*3)
            else:
                pass

    def __set_default_hp(self):
        self.hp = self.lvl ** (1 + 0.3) ** 2 + 499
        return self.hp

    def __set_default_attack(self):
        self.attack = self.lvl ** (1 + 0.3) ** 2 + 9
        return self.attack

    def __set_default_defence(self):
        self.attack = self.lvl ** (1 + 0.3) ** 2 + 9
        return self.attack

    def __get_status_from_item(self, atk, defend):
        bonus_hp_from_def = defend * 5
        self.hp += int(bonus_hp_from_def)
        self.attack += atk
        self.defense += defend

    def _get_slots(self):
        self.hero_slots = get_hero_slots_from_db()
        return self.hero_slots


class Item:
    """Used to connect and get from the PostgresQl database."""

    __ITEM_RARITY = {
        0: 'Normal',
        1: 'Rare',
        2: 'Mythical',
        3: 'Legendary'
    }

    def __init__(self, item_name, hero_name):
        psycopg2.extras.register_uuid()
        self.item_id = uuid.uuid4()
        self.item_name = item_name
        self.hero_name = hero_name
        self.item_type = item_type
        self.rarity = rarity
        self.item_lvl = item_lvl
        self.item_attack = item_attack
        self.item_defense = item_defense
        self.equipped = equipped

    def __repr__(self):
        return f"""
                Character <{self.hero_name}>
                item_id {self.item_id}
                item_name: {self.item_name}
                item_lvl: {self.item_lvl} 
                item_type: {self.item_type}
                rarity: {self.__ITEM_RARITY[self.rarity]}
                attack: {self.item_attack}
                defense: {self.item_defense}
                equipped: {self.equipped}
                """