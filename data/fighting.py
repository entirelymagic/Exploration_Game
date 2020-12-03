class Fighting:
    def __init__(self, hero, monster):

        self.hero = hero
        self.monster = monster
        self.winner = None
        self.rounds = 1
        self.__get_winner()
        # TODO finish class

    def __get_winner(self):
        hero_hp_left = self.hero.hp - self.monster.attack
        monster_hp_left = self.monster.hp - self.hero.attack

        while hero_hp_left >= 0 and monster_hp_left >= 0:
            hero_hp_left = hero_hp_left - self.monster.attack
            monster_hp_left = monster_hp_left - self.hero.attack
            self.rounds += 1
        else:
            self.hero.hp = hero_hp_left
        if hero_hp_left > monster_hp_left:
            self.winner = self.hero.hero_name
            return self.winner
        else:
            self.winner = self.monster.name
            return self.winner


