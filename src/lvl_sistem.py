def xp_needed_for_the_next_lvl(lvl_provided):
    """
    Giving the lvl provided this function calculates the total xp needed
    to level up to the next one."""
    LVL_System = {1: 100}
    lvl: int = 1
    xp = 100
    needed_xp = 100
    for i in range(1, 101):
        increased = lvl**(1+0.5)**2
        xp = xp+increased
        needed_xp += xp
        lvl += 1
        # print(f'Total Xp needed for lvl: {lvl} : {int(needed_xp)} xp, difference needed: {int(xp)},')
        LVL_System[lvl] = int(needed_xp)
    if lvl_provided in LVL_System:
        return LVL_System[lvl_provided+1]


