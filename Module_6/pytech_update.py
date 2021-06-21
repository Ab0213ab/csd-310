# Andrew Schaefer
# 6/22/21
# CSD310 Mod 6.2

# Imports Pymongo tools
import pymongo 

# Connects to MongoDB database
myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.zcfrz.mongodb.net/pytech?retryWrites=true&w=majority")
mydb = myclient["pytech"]
mycol = mydb["students"]

# Finds all pytech.students documents and displays them
x = mycol.find()
print(list(x))

# Updates last name of student with student_id 1007
mycol.update_one({"student_id": 1007}, {"$set": {"last_name": "Mercury"}})

# Finds and displays newly updated document
x = mycol.find_one({"student_id": 1007})
print(x)

