import pymongo
from app.db.mongodb import DATABASE

def new_office(new_office_var):
    DATABASE.offices.insert_one(new_office_var)

def find_all_offices ():
    result = list(DATABASE.offices.find({}, {'_id': False}))
    return result