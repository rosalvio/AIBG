from Team import *

team0 = Team(0)
team0.members = [Soldier.mock_soldier(0), Soldier.mock_soldier(0)]

team0.set_soldiers_spawn()

for soldier in team0.members:
    print(soldier.pos)

