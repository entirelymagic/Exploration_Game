USER_CHOICE = """
1. Start an Adventure
2. View Inventory
3. View HeroStats
4. Quit
"""

ADVENTURE_CHOICE = """
1.Attack the monster.
2.Use Potion to heal.
2.Go back to main menu.
"""

INVENTORY_CHOICE = """
1. Select item number to equip.
2. Go back to main menu.
"""

MENU_BAR = {  # TODO menu bar actions
    "adventure": "adventure_choice",
    "inventory": "present_inventory",
    "hero_stats": "preset_hero_stats",
    "quit": "quit"
}

ADVENTURE_BAR = {
    "attack": "attack",
    "heal": "heal",
    "go_back": "go_back"
}

INVENTORY_BAR = {
    "select_item": "select_item",
    "go_back": "go_back"
}

