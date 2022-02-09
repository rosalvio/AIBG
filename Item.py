from Soldier import Soldier


class Item:

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @staticmethod
    def effect(target: Soldier):
        pass


class AmmoPack(Item):

    def __init__(self):
        super().__init__("AmmoPack", 2)

    @property
    def name(self):
        return super().name

    @staticmethod
    def effect(target: Soldier):
        target.ammo_packs = target.ammo_packs + 1