from src.data_types import Items, Heroes, HeroSlots
from random import randint, choice


class CreateItems:
    """
    Create an item giving the item <lvl> (according to the character and item_type
    Can be offensive <value=1> or defensive with <value=0>
    """
    def __init__(self, item_lvl, item_type):
        self.item_lvl = self.__item_lvl(item_lvl)
        self.item_type = self.__item_type(item_type)
        self.rarity = self.__get_rarity()
        self.attack = int(self.__attack()/randint(20, 25) * randint(20, 25))
        self.defense = int(self.__attack()/randint(20, 25) * randint(20, 25))
        self.name = str(self.__name())

    def __repr__(self):
        return f"""
                Item_lvl: <{self.item_lvl}>
                item_id: {self.item_type}
                item_rarity: {self.rarity}
                item_attack: {self.attack}
                item_defense: {self.defense}
                item_name: {self.name}
                """

    # Defensive type of weapons
    DEF_TYPE = [
        'Helmet',
        'Shied',
        'Belt',
        'Body',
        'Pants',
        'Boots',
        'Arms'
    ]
    # Offensive type of weapons
    OFF_TYPE = [
        'One hand weapon',
        'Two handed weapon',
        'Ring',
        'Amulet',
    ]

    @staticmethod
    def __get_rarity():
        luck = randint(0, 100)
        if luck <= 75:
            result = 0
        elif luck <= 90:
            result = 1
        elif luck <= 97:
            result = 2
        else:
            result = 3
        return result

    def __item_type(self, item_type):
        if item_type == 0:
            result = choice(self.DEF_TYPE)
            return result
        elif item_type == 1:
            result = choice(self.OFF_TYPE)
            return result

    @classmethod
    def __item_lvl(cls, lvl):
        if lvl >= 3:
            result = randint(lvl-2, lvl+1)
            return result
        else:
            return lvl

    def __attack(self):
        lvl = self.item_lvl
        if self.rarity == 0:
            t = lvl**(1+0.35)**2 + randint(3, 7)
            return t
        elif self.rarity == 1:
            t1 = lvl**(1+0.37)**2 + randint(3, 9)
            return t1
        elif self.rarity == 2:
            t2 = lvl**(1+0.41)**2 + randint(5, 10)
            return t2
        elif self.rarity == 3:
            t3 = lvl**(1+0.45)**2 + randint(7, 15)
            return t3

    def __name(self):
        NAME = {
            0: 'Wood',
            1: 'Bronze',
            2: 'Iron',
            3: 'Titanium',
        }

        EXTRA_NAMES = [
            'of King Warlock',
            'of Death',
            'of Shaman King'
            'Slayer',
            'from Poney Land'
        ]
        if self.rarity in NAME.keys():
            item_name = NAME[self.rarity]+' '+self.item_type
            if self.rarity == 3:
                item_name = item_name+' '+choice(EXTRA_NAMES)
                return item_name
            else:
                return item_name

    def add_to_db(self, hero_name):
        """Add the newly created item to the database"""
        if self.item_type in self.OFF_TYPE:
            item = Items(self.name, hero_name, self.item_type, self.rarity, self.item_lvl, item_attack=self.attack)
            item.create_new_item()
        elif self.item_type in self.DEF_TYPE:
            item = Items(self.name, hero_name, self.item_type, self.rarity, self.item_lvl, item_defense=self.defense)
            item.create_new_item()


class CreateMonster:
    """Create a monster according to the lvl of the character"""
    def __init__(self, lvl):
        self.name = self.__pick_monster_name()
        self.lvl = self.__item_lvl(lvl)
        self.hp = int(self.__get_hp())
        self.attack = int(self.__get_attack()/randint(20, 30) * randint(20, 30))
        self.defense = int(self.__get_attack()/randint(20, 30) * randint(20, 30))

    def __repr__(self):
        return f"""
        Monster name : {self.name}
        Monster lvl: {self.lvl}
        Monster HP: {self.hp}
        Monster ATK: {self.attack}
        Monster DEF: {self.defense}
        """

    @classmethod
    def __item_lvl(cls, lvl):
        result = randint(lvl, lvl + 3)
        return result

    MONSTER_NAMES = [
        'Rat',
        'Wolf',
        'Golem',
        'Troll',
        'Giant Spider',
        'Bear',
        'Zombie',

    ]

    def __pick_monster_name(self):
        return choice(self.MONSTER_NAMES)

    def __get_hp(self):
        return (self.lvl**(1+0.35)**2)*20

    def __get_attack(self):
        return self.lvl**(1+0.35)**2


class HeroStats(Heroes, HeroSlots):
    """Gather and get the hero statistics"""
    def __init__(self, hero_name, account, lvl=1, hp=500, attack=10, defense=10, fire_attack=0, fire_res=0,
                 stash_size=50):
        # super().__init__(hero_name, account, lvl, hp, attack, defense, fire_attack, fire_res, stash_size)
        self.hero_name = hero_name
        self.account = account
        self.stash_size = stash_size
        self.lvl = lvl
        self.hp = self.__set_default_hp()
        self.attack = self.__set_default_attack()
        self.defense = self.__set_default_defence()
        self.fire_res = fire_res
        self.fire_attack = fire_attack
        self.hero_slots = self._get_slots()
        self.items = self.__get_hero_items()
        self._get_status_for_equipped_items()
        self.currentHP = self.hp

    autoEquip = True

    def __repr__(self):
        return f"""Character <{self.hero_name}>
                lvl: {self.lvl}
                hp: {self.currentHP}
                max_HP: {self.hp}
                attack: {self.attack}
                defense: {self.defense}
                fire attack: {self.fire_attack}
                fire resist: {self.fire_res}
                account: {self.account}
                items: {self.items}
                """

    def _set_item_active(self, itemID):
        for item in self.items:
            if item[0] == itemID:
                if not item[5]:
                    item[5] = True
                    self.hero_slots[item[3]] = 1

    def __get_hero_items(self):
        self.items = Items.load_item_from_db_by_hero_name(self.hero_name)
        return self.items

    def update_equipped_status_to_True(self, item, slot):
        item[5] = True
        self.hero_slots[slot] = 1
        self._update_slots()
        Items.update_item_status(item[0], True)

    def _get_status_for_equipped_items(self):
        slots = self.hero_slots.keys()
        for item in self.items:
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
        self.hp = self.lvl**(1+0.3)**2 + 499
        return self.hp

    def __set_default_attack(self):
        self.attack = self.lvl**(1+0.3)**2 + 9
        return self.attack

    def __set_default_defence(self):
        self.attack = self.lvl**(1+0.3)**2 + 9
        return self.attack

    def __get_status_from_item(self, atk, defend):
        bonus_hp_from_def = defend * 5
        self.hp += int(bonus_hp_from_def)
        self.attack += atk
        self.defense += defend

    def _get_slots(self):
        slots = HeroSlots(self.hero_name)
        slots.get_hero_slots_from_db()
        self.hero_slots = slots.hero_slots
        return self.hero_slots

    def _update_slots(self):
        self.update_slots_db()


