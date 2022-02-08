from Item import Item
from Soldier import Soldier


class AmmoPack(Item):

    def __init__(self):
        super().__init__("AmmoPack")

    @property
    def name(self):
        return super().name

    @staticmethod
    def effect(target: Soldier):
        target.ammo_packs = target.ammo_packs + 1
