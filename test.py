from Item import *
from Soldier import Soldier
from Weapon import *

a = AmmoPack()
sn = Sniper()

s = Soldier({a: (2, 1)}, sn, 1)

print(s.speed)
