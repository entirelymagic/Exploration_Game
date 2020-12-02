from data.data_types import Items, Heroes
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
        self.attack = int(self.__attack())
        self.defense = int(self.__attack()/2)
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
        if luck <= 25:
            result = 0
        elif luck <= 50:
            result = 1
        elif luck <= 90:
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
        result = randint(lvl - 2, lvl + 1)
        return result

    def __attack(self):
        lvl = self.item_lvl
        rarity = self.rarity
        if rarity == 0:
            t = lvl + randint(2, 5)
            return t
        elif rarity == 1:
            t = lvl + randint(2, 5)
            return t
        elif rarity == 2:
            t = lvl*1.6 + randint(3, 10)
            return t
        elif rarity == 3:
            t = lvl*1.9 + randint(7, 15)
            return t

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
            item = Items(self.name, hero_name, self.item_type, self.rarity, self.item_lvl, self.attack)
        elif self.item_type in self.DEF_TYPE:
            item = Items(self.name, hero_name, self.item_type, self.rarity, self.item_lvl, self.defense)
        item.create_new_item()


class CreateMonster:
    """Create a monster according to the lvl of the character"""
    def __init__(self, lvl):
        self.name = self.__pick_monster_name()
        self.lvl = self.__item_lvl(lvl)
        self.hp = self.__get_hp()
        self.attack = int(self.__get_attack())
        self.defense = int(self.__get_attack()/2)

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
        return self.lvl*(1+4)**2

    def __get_attack(self):
        return self.lvl+randint(1, 3)


class HeroStats(Heroes):
    """Gather and get the hero statistics"""
    def __init__(self, hero_name, account, lvl=1, hp=500, attack=10, defense=10, fire_attack=0, fire_res=0,
                 stash_size=50):
        # super().__init__(hero_name, account, lvl, hp, attack, defense, fire_attack, fire_res, stash_size)
        self.hero_name = hero_name
        self.lvl = lvl
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.fire_res = fire_res
        self.fire_attack = fire_attack
        self.account = account
        self.stash_size = stash_size
        self.items = self.__get_hero_items()

    hero_slots = {
        'Helmet': 0,
        'Belt': 0,
        'Pants': 0,
        'Boots': 0,
        'Arms': 0,
        'Chest': 0,
        'Left_arm': 0,
        'Right_arm': 0,
        'Left_ring': 0,
        'Right_ring': 0,
        'Amulet': 0,
    }

    def __repr__(self):
        return f"""Character <{self.hero_name}>
                lvl: {self.lvl}
                hp: {self.hp} 
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

    def __autoequip_items(self):
        pass   # TODO make autoequip function active
