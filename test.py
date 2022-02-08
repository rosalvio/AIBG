from Sniper import Sniper
from AmmoPack import AmmoPack
from Soldier import Soldier

a = AmmoPack()
sn = Sniper()

s = Soldier({a: (2, 1)}, sn, 1)

print(s.speed)
