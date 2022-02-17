import pymongo
from app.db.mongodb import DATABASE

def find_one():
    result = DATABASE.benefits.find_one({}, {'_id': False})
    print(result)
    return result