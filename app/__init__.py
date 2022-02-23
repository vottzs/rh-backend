from flask import Flask
from flask_cors import CORS
from app.views import add_views
  
def create_app():
  """
  Create and configure a Flask app
  """
  app = Flask(__name__)
  app.config.from_object(__name__)
  CORS(app)
  # inform what are the urls accepted and what to do with it
  add_views(app)
  return app
