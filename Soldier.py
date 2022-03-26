from functools import reduce
from Weapon import *
from Item import *
from math import sqrt

BASE_SPEED = 0.4
BASE_HEALTH = 100
BASE_INVENTORY = {}  # Los objetos son diccionarios con clave Item y valor cantidad
WEIGHT_CONSTANT = 0.8


class Soldier:

    @staticmethod
    def mock_soldier(team: int):
        return Soldier({AmmoPack(): 3}, Sniper(), team)

    def __init__(self, inventory: dict[Item, int], weapon: Weapon, team: int):
        self._weight = 0
        self._inventory = inventory
        self._weapon = weapon
        self.weight = self.new_weight()
        self._health = BASE_HEALTH
        self._speed = self.new_speed()
        self._has_flag = False
        self._team = team
        self._pos = (0, 0)
        self._destination = self.pos
        # TODO Anyadir id del soldado

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, new):
        self._pos = new

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
        return reduce(lambda x, y: x + y, [k.weight * v for k, v in self.inventory.items()])

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
        return max(0, BASE_SPEED - self.weight)

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
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, val):
        self._destination = val

    def use_item(self, item_name):
        aux = self.inventory[item_name]
        aux = aux - 1
        if aux == 0:
            del self.inventory[item_name]
        else:
            self.inventory[item_name] = aux
            if item_name == "HealthUp":
                self.health += 50
                if self.healt > 100:
                    self.health = 100

    def move(self):
        if round(self.pos[0]) != self.destination[0]:
            self.pos = (self.pos[0] + self.speed, self.pos[1])
        if round(self.pos[1]) != self.destination[1]:
            self.pos = (self.pos[0], self.pos[1] + self.speed)

    def distance(self, target):
        return sqrt((self.pos[0] - target.pos[0])**2 + (self.pos[1] - self.pos[1])**2)
