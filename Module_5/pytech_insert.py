# Andrew Schaefer
# 6/13/21
# CSD310 Mod 5

import pymongo 
from pymongo import MongoClient 
url = "mongodb+srv://admin:admin@cluster0.zcfrz.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())