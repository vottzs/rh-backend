import pymongo
from app.db.mongodb import DATABASE

def new_hiring_type(new_hiring_type_var):
    DATABASE.hiring_types.insert_one(new_hiring_type_var)

def find_all_hiring_types ():
    result = list(DATABASE.hiring_types.find({}))
    for item in result:
        item['creation_date'] = item['_id'].generation_time
        del item['_id']
    return result
