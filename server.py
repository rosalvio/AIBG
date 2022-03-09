from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
from Soldier import Soldier
from Team import Team

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('soldier', help='Pasa su equipo.')


class AddSoldier(Resource):

    def post(self):
        args = parser.parse_args()
        print(args)
        res = {'team': args['soldier']}
        return res, 201


api.add_resource(AddSoldier, '/')


if __name__ == '__main__':
    app.run(debug=True)
