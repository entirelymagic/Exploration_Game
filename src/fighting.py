class Fighting:
    def __init__(self, hero, monster):

        self.hero = hero
        self.monster = monster
        self.winner = None
        self.rounds = 1
        self.__get_winner()
        # TODO finish class

    def __get_winner(self):
        """Take hero and monster attack and hp and calculate and return the winner  and set the
        remaining HP left for the hero .
        Each round the attack of the hero and monster are draw from the HP of opposite.
        """
        hero_hp_left = self.hero.currentHP - self.monster.attack
        monster_hp_left = self.monster.hp - self.hero.attack

        while hero_hp_left >= 0 and monster_hp_left >= 0:
            hero_hp_left = hero_hp_left - self.monster.attack
            monster_hp_left = monster_hp_left - self.hero.attack
            self.rounds += 1
        else:
            if self.hero.currentHP < 0:
                self.hero.currentHP = 0
            else:
                self.hero.currentHP = hero_hp_left
        if hero_hp_left > monster_hp_left:
            self.winner = self.hero.hero_name
            return self.winner
        else:
            self.winner = self.monster.name
            return self.winner


