from flask import Flask
from flask_cors import CORS
from app.views import add_views
  
def create_app():
  app = Flask(__name__)
  app.config.from_object(__name__)
  CORS(app)
  add_views(app)
  return app
