# Andrew Schaefer
# 6/13/21
# CSD310 Mod 5.3 (b)..

import pymongo 

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.zcfrz.mongodb.net/pytech?retryWrites=true&w=majority")
mydb = myclient["pytech"]
mycol = mydb["students"]

for x in mycol.find():
    print(x)

x = mycol.find_one({"student_id" : 1007})
print(x)