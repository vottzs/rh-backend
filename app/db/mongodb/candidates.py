import pymongo
from app.db.mongodb import DATABASE

def find_all ():
    result = list(DATABASE.candidates.find({}, {'_id': False}))
    return result

def find_by_stage(Stage):
    result = list(DATABASE.candidates.find({'Stage': Stage}, {'_id': False}))
    return result

def find_one(candidate_id):
    result = DATABASE.candidates.find_one({'id': candidate_id}, {'_id': False})
    return result

def move_candidate(candidate_id, Stage):
    DATABASE.candidates.update_one({'id': candidate_id}, {'$set': {'Stage': Stage}})