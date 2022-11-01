from pytrends.request import TrendReq
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.google_trends

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Bitcoin", "NFT"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

df = pytrends.interest_over_time()
# print(df.head())

for i, row in df.iterrows():
    db.blockchain.insert_one(
        {'_id': i, 'bitcoin': row['Bitcoin'], 'nft': row['NFT']})
    pass
