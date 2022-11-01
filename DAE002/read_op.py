from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.google_trends
cursor = db.openrice.find({
    '$and': [
        {'name': {'$all': ["Green Orange"]}}
    ]
})

for doc in cursor:
    print(doc)
