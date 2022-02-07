import Item
from Soldier import Soldier


class AmmoPack(Item):

    def __init__(self):
        super("AmmoPack")

    @staticmethod
    def effect(target: Soldier):
        target.ammo_packs = target.ammo_packs + 1
