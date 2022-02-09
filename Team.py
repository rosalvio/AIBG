from Soldier import Soldier
MAX_TEAM = 5


class Team:

    def __init__(self, tid: int):
        self._members: list[Soldier] = []
        self._tid = tid
        self._base = self.get_base()

    def get_base(self):
        if self.tid == 0:
            return 10, 10
        else:
            return 590, 890

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

    @property
    def base(self):
        return self._base