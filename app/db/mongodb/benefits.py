"""
All database operations related to benefits.
"""
from app.db.mongodb import DATABASE

def parse_benefits(benefits):
    for item in benefits:
        item['_id'] = str(item['_id'])

def new_benefit(new_benefit_var):
    """
    Creates  a new office.
    Args:
        new_benefit_var (dict): new benefit information
    """
    DATABASE.benefits.insert_one(new_benefit_var)

def find_all_benefits ():
    """
    Returns all offices from database
    """
    result = list(DATABASE.benefits.find({}))
    for item in result:
        #for every ObjectId transforms the _Id in a creation date
        item['creation_date'] = item['_id'].generation_time
    parse_benefits(result)
    return result
