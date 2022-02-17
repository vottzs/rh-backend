import pymongo
from app.db.mongodb import DATABASE

def new_benefit(new_benefit_var):
    DATABASE.benefits.insert_one(new_benefit_var)

def find_all_benefits ():
    result = list(DATABASE.benefits.find({}))
    for item in result:
        item['creation_date'] = item['_id'].generation_time
        del item['_id']
    return result
