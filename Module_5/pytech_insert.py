# Andrew Schaefer
# 6/13/21
# CSD310 Mod 5.3 (a)

import pymongo 

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.zcfrz.mongodb.net/pytech?retryWrites=true&w=majority")
mydb = myclient["pytech"]
mycol = mydb["students"]

data_1 = [{
    "student_id" : 1007, "first_name" : "Fred", "last_name" : "Flintstone"
}]
x = mycol.insert_many(data_1)
print(x.inserted_ids)

data_2 = [{
    "student_id" : 1008, "first_name" : "Bernie", "last_name" : "Sanders"
}]
y = mycol.insert_many(data_2)
print(y.inserted_ids)

data_3 = [{
    "student_id" : 1009, "first_name" : "Christopher", "last_name" : "Hitchens"
}]
z = mycol.insert_many(data_3)
print(z.inserted_ids)



