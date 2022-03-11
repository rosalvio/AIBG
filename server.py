from flask import Flask, request
from flask_restful import Resource, Api
import json
from Soldier import Soldier
from Team import Team
from Item import *

app = Flask(__name__)
api = Api(app)



class AddSoldier(Resource):

    def post(self):
        l = request.get_json()
        for soldier in l:
            print(soldier['team'])
        res = {'team': "done"}
        return res, 201


api.add_resource(AddSoldier, '/')


if __name__ == '__main__':
    app.run(debug=True)
