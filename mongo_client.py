import pymongo

from config import MONGO_HOST, MONGO_PORT, MONGO_DB

client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client[MONGO_DB]
collection = db.gg_three_years