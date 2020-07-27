# import required libraries
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from app.PredictGame import PredictGame
from app.ListGames import ListGames

# instantiate flask server
app = Flask(__name__)
api = Api(app)

CORS(app)

# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictGame, '/game')
api.add_resource(ListGames, '/games')
