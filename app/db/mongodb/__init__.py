import pymongo
import os
# contains the url for database connection
CONNECTION_STRING = os.environ.get('GRHCONNECTIONSTRING')
# create a connection to gestaorh database
DATABASE = pymongo.MongoClient(CONNECTION_STRING).gestaorh
