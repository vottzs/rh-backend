import pymongo
DATABASE = pymongo.MongoClient("mongodb+srv://guillass:Minhasenha@cluster0.x1kqu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").gestaorh

def find_one():
    result = DATABASE.default_hiring_stages.find_one({}, {'_id': False})
    print(result)
    return result

testando = DATABASE.default_hiring_stages.find_one({}, {'_id': False})
print(testando)