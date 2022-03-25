from flask import Flask, request
from flask_restful import Resource, Api
# Fuck ngrok, que me pasen el codigo y lo corro yo.
import json
from Soldier import Soldier
from Team import Team
from Item import *
from Weapon import *
from game import *

app = Flask(__name__)
api = Api(app)
team: list[Soldier] = []


class AddSoldier(Resource):

    def post(self):
        soldiers_list = request.get_json()
        for soldier in soldiers_list:
            t = soldier['team']
            inv = soldier['inventory']
            final_inv = dict()
            for item, amount in inv.items():
                final_inv[items[item]] = amount
            print(final_inv)
            weapon = weapons[soldier['weapon']]
            print(weapon.name())
            team.append(Soldier(final_inv, weapon, soldier['team']))

        if len(team) == 5:
            team_obj = Team(t)
            team_obj.members = team

        return {'team': [x.team for x in team]}, 201


class GetFOV(Resource):

    def get(self, soldier_id):
        # TODO Devolver lista de enemigos visibles.
        return {'id': soldier_id}, 201


class Shoot(Resource):

    def post(self, shooter_id, target_id):
        # TODO Solo si target esta en la lista del fov de shooter
        return {'shooter': shooter_id, 'target': target_id}, 201


api.add_resource(AddSoldier, '/')
api.add_resource(GetFOV, '/fov/<int:soldier_id>')
api.add_resource(Shoot, '/shoot/<int:shooter_id>/<int:target_id>')


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
