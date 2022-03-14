from flask import Flask, request
from flask_restful import Resource, Api
# Fuck ngrok, que me pasen el codigo y lo corro yo.
import json
from Soldier import Soldier
from Team import Team
from Item import *
from Weapon import *

app = Flask(__name__)
api = Api(app)


class AddSoldier(Resource):

    def post(self):
        l = request.get_json()
        for soldier in l:
            print(soldier['team'])
        # TODO Crear objeto Soldier con cada clave del diccionario.
        return 201


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
    app.run(debug=True, host='0.0.0.0')
