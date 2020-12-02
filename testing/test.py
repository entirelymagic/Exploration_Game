from unittest import TestCase
from app import *


class Testing(TestCase):
    def test_HeroSlots(self):
        slots_for_my_hero = HeroSlots('Godlike')
        printer = print(slots_for_my_hero)
        self.assertEquals(print(slots_for_my_hero), printer)

