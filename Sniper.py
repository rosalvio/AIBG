from Weapon import Weapon

AMMO = 10
RANGE = 50


class Sniper(Weapon):

    def __init__(self):
        self._name = "Sniper"
        self._ammo = AMMO
        self._range = RANGE

    def name(self):
        return self._name

    def ammo(self):
        return self._ammo

    def range(self):
        return self._range
