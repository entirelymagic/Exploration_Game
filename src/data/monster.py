class Monster:
    """Create a random lvl monster according to the lvl provided"""

    __MONSTER_NAMES = [
        'Rat',
        'Wolf',
        'Golem',
        'Troll',
        'Giant Spider',
        'Bear',
        'Zombie',
    ]

    def __init__(self, lvl):
        self.name = self.__pick_monster_name()
        self.lvl = self.__monster_lvl(lvl)
        self.hp = int(self.__get_hp())
        self.attack = int(self.__get_attack() / randint(20, 30) * randint(20, 30))
        self.defense = int(self.__get_attack() / randint(20, 30) * randint(20, 30))
        self.xp = self.__get_xp()

    def __repr__(self):
        return f"""
        Monster name : {self.name}
        Monster lvl: {self.lvl}
        Monster HP: {self.hp}
        Monster ATK: {self.attack}
        Monster DEF: {self.defense}
        """

    @staticmethod
    def __monster_lvl(lvl):
        """Create a random lvl for the monster"""
        if lvl >= 2:
            min_lvl = lvl - 1
        else:
            min_lvl = 1
        return randint(min_lvl, lvl + 3)

    def __pick_monster_name(self):
        return choice(self.__MONSTER_NAMES)

    def __get_hp(self):
        return (self.lvl ** (1 + 0.35) ** 2) * 20

    def __get_attack(self):
        return self.lvl ** (1 + 0.35) ** 20

    def __get_xp(self):
        return self.lvl ** (1 + 0.35) ** 2