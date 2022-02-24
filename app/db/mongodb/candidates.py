from this import d
import pymongo
DATABASE = pymongo.MongoClient("mongodb+srv://guillass:Minhasenha@cluster0.x1kqu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").gestaorh

def find_all():
    result = list(DATABASE.candidates.find({}, {'_id': False}))
    return result

def find_by_stage(stage):
    result = list(DATABASE.candidates.find({'stage':stage}, {'_id': False}))
    return result

def find_one(candidate_id):
    result = (DATABASE.candidates.find_one({'id': candidate_id}, {'_id': False}))
    return result

def move_candidate(candidate_id,stage):
    DATABASE.candidates.update_one({'id': candidate_id}, {'$set': {'stage': stage}})
