from data.data_types import Items
from random import randint, choice


class CreateItems:
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

    DEF_TYPE = [
        'Helmet',
        'Shied',
        'Belt',
        'Body',
        'Pants',
        'Boots',
        'Arms'
    ]
    OFF_TYPE = [
        'One hand weapon',
        'Two handed weapon',
        'Ring',
        'Amulet',
    ]

    def __get_rarity(self):
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
        if self.item_type in self.OFF_TYPE:
            item = Items(self.name, hero_name, self.item_type, self.rarity, self.item_lvl, self.attack)
        elif self.item_type in self.DEF_TYPE:
            item = Items(self.name, hero_name, self.item_type, self.rarity, self.item_lvl, self.defense)
        item.create_new_item()



