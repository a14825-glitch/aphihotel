from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {"hotel_id": "paraiso":"nome":"hotel paraiso","estrelas":4.6,"diaria":123.99, "cidade": "Porto" },
    {"hotel_id": "fukui":"nome":"fukui resort","estrelas":4.8,"diaria":225.99, "cidade": "Viena" },
    {"hotel_id": "aguas":"nome":"hotel aguas","estrelas":4.2,"diaria":193.99, "cidade": "Lisboa" },
]

class hoteis(Resource):

# Rotas
api.add_resource(Hoteis,"/hoteis")

if __name__ == "__main__":
    app.run(debug=True)
    return{ "hoteis": hoteis}
