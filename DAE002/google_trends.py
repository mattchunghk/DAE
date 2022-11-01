from pytrends.request import TrendReq
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.google_trends

cursor = db.blockchain.find({"$and": [{"bitcoin"}]})
