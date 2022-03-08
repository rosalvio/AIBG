from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()


class AddSoldier(Resource):

    parser.add_argument('soldier', help='Pasa su equipo.')

    def post(self):
        json_req = request.get_json()
        return {'You sent ': json_req}


api.add_resource(AddSoldier, '/')


if __name__ == '__main__':
    app.run(debug=True)
