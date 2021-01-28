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

    @staticmethod
    def __item_lvl(lvl):
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
            item = Item(self.name, hero_name, self.item_type, self.rarity, self.item_lvl, item_attack=self.attack)
            item.create_new_item()
        elif self.item_type in self.DEF_TYPE:
            item = Item(self.name, hero_name, self.item_type, self.rarity, self.item_lvl, item_defense=self.defense)
            item.create_new_item()