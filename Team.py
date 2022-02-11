from Soldier import Soldier
from random import Random
MAX_TEAM = 5


class Team:

    def __init__(self, tid: int):
        self._members: list[Soldier] = []
        self._tid = tid
        self._base = self.get_base()

    def get_base(self):
        if self.tid == 0:
            return 101, 101
        else:
            return 1099, 699

    @property
    def tid(self):
        return self._tid

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, array):
        # TODO Anyadir comprobaciones max soldados y max objetos
        self._members = array
        self.set_soldiers_spawn()

    @property
    def base(self):
        return self._base

    def set_soldiers_spawn(self):
        rand = Random()
        used_positions = []
        for soldier in self.members:
            aux = self.base[0] + rand.randint(-100, 100), self.base[1] + rand.randint(-100, 100)
            if aux not in used_positions:
                soldier.pos = aux
                used_positions.append(aux)
