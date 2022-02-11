import pymongo
DATABASE = pymongo.MongoClient("mongodb+srv://leo_rh:Lobo@cluster0.286wa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").gestaorh

def find_one():
    result = DATABASE.default_hiring_stages.find_one({}, {'_id': False})
    print(result)
    return result