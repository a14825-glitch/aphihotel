from flask import Flask
from flask_restful import Resource, Api
from Resource.hotel import Hoteis, Hotel

#variavel representar a minha aplicaçao
app = Flask(__name__)
api = Api(app)

# rotas 

api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel,"/hoteis/<string:id_hotel>")

if __name__  == "__main__":
    app.run(debug=True)
