from app.db.mongodb import DATABASE

def find_one():
    result = DATABASE.default_hiring_stages.find_one({}, {'_id': False})
    return result