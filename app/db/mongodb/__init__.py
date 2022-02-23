import pymongo
import os
CONNECTION_STRING = os.environ.get('GRHCONNECTIONSTRING')
DATABASE = pymongo.MongoClient(CONNECTION_STRING).gestaorh
