"""
7 8 6
16 19 7 11 23 8 16
"""
_, hit_dmg, seconds = [int(p) for p in input().split()]
monsters = [int(p) for p in input().split()]

monsters_killed = 0
for monst in sorted(monsters):
    needed_hits = 0
    if monst % hit_dmg != 0:
        needed_hits = (monst // hit_dmg) + 1
    else:
        needed_hits = monst // hit_dmg
    seconds -= needed_hits
    if seconds >= 0:
        monsters_killed += 1
    else:
        break

print(monsters_killed)
