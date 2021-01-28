from unittest import TestCase
from app import *
from src.lvl_sistem import xp_needed_for_the_next_lvl


def startConn(test):
    def wrapper(*args, **kwargs):
        Database.initialise(database=database_name,
                            user=user_name,
                            password=user_password,
                            host=host_name,
                            port=5432)
        test(*args, **kwargs)
        Database.close_all_connections()

    return wrapper


class Testing(TestCase):
    @startConn
    def test_HeroSlots(self):
        slots_for_my_hero = HeroSlots('Godlike')
        slots_after_db = slots_for_my_hero.get_hero_slots_from_db()
        slots_for_my_hero.update_slots_db()
        self.assertNotEqual(slots_for_my_hero, slots_after_db)

    @startConn
    def test_HeroStats(self):
        my_hero = HeroStats('Godlike', 'elvis.munteanu@gmail.com')
        items = my_hero.items
        type(items)

    def test_CreateItems(self):
        for i in (10, 30, 100):
            new_item = CreateItems(i, 0)
            new_item3 = CreateItems(i, 1)

    def test_CreateMonsters(self):
        for i in (10, 100):
            new_item = CreateMonster(i)
            # print(new_item)

    def test_get_xp(self):
        result = 22901683
        self.assertEqual(get_xp_needed(99), result)

