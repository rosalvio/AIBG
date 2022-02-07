from functools import reduce
from Weapon import Weapon

BASE_SPEED = 50
BASE_HEALTH = 100
BASE_INVENTORY = {}  # Los objetos son diccionarios con clave nombre y valor tupla (cantidad, peso)
WEIGHT_CONSTANT = 0.8


class Soldier:

    def __init__(self, inventory: dict, weapon: Weapon, team):
        self._ammo_packs = 0
        self._inventory = inventory
        self._weapon = weapon
        self._weight = self.new_weight()
        self._health = BASE_HEALTH
        self._speed = self.new_speed()
        self._has_flag = False
        self._team = team

    @property
    def weight(self):
        """
        :return: Peso que lleva el soldado.
        """
        return self._weight

    @weight.setter
    def weight(self, new):
        self._weight = new

    def new_weight(self):
        return self.weight(reduce(lambda x, y: x + y, [v[0] * v[1] for v in self.inventory.values()]))

    @property
    def speed(self):
        """
        :return: Velocidad del soldado ya modificada por peso.
        """
        return self._speed

    @speed.setter
    def speed(self, new):
        self._speed = new

    def new_speed(self):
        return BASE_SPEED - (WEIGHT_CONSTANT * self.weight)

    @property
    def inventory(self):
        """
        :return: Inventario actual del soldado.
        """
        return self._inventory

    @inventory.setter
    def inventory(self, new):
        self._inventory = new

    @property
    def health(self):
        """
        :return: Vida actual del soldado.
        """
        return self._health

    @health.setter
    def health(self, new):
        self._health = new

    @property
    def weapon(self):
        """
        :return: Armas del soldado (Max 2).
        """
        return self._weapon

    @weapon.setter
    def weapon(self, new: Weapon):
        self._weapon = new

    @property
    def has_flag(self):
        """
        :return: True si el soldado lleva la bandera.
        """
        return self._has_flag

    @has_flag.setter
    def has_flag(self, new):
        self._has_flag = new

    @property
    def team(self):
        """
        :return: Equipo del soldado.
        """
        return self._team

    @team.setter
    def team(self, val):
        self._team = val

    @property
    def ammo_packs(self):
        return self._ammo_packs

    @ammo_packs.setter
    def ammo_packs(self, new_amount):
        self._ammo_packs = new_amount

    def use_item(self, item_name):
        aux = self.inventory[item_name]
        new_amount = aux[0] - 1
        if new_amount == 0:
            del self.inventory[item_name]
        else:
            self.inventory[item_name] = (new_amount, aux[1])

