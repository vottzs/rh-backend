"""
All database operations related to hiring types.
"""
from app.db.mongodb import DATABASE

def new_hiring_type(new_hiring_type_var):
    """
    Returns all hiring types from database
    """
    DATABASE.hiring_types.insert_one(new_hiring_type_var)

def find_all_hiring_types ():
    result = list(DATABASE.hiring_types.find({}))
    for item in result:
         #for every ObjectId transforms the _Id in a creation date
        item['creation_date'] = item['_id'].generation_time
        #deletes the ObjectId in the result cause it isn't serializable
        del item['_id']
    return result
