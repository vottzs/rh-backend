from flask import Flask
  
def create_app():
  app = Flask(__name__)
  app.config.from_object(__name__)
  return app
