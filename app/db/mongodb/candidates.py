import pymongo
from app.db.mongodb import DATABASE

def find_all ():
    result = list(DATABASE.candidates.find({}, {'_id': False}))
    return result

def find_by_stage(stage):
    result = list(DATABASE.candidates.find({'stage': stage}, {'_id': False}))
    return result

def find_one(candidate_id):
    result = DATABASE.candidates.find_one({'id': candidate_id}, {'_id': False})
    return result

def move_candidate(candidate_id, stage):
    DATABASE.candidates.update_one({'id': candidate_id}, {'$set': {'stage': stage}})