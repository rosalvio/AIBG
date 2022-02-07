from Soldier import Soldier


class Item:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @staticmethod
    def effect(target: Soldier):
        pass
