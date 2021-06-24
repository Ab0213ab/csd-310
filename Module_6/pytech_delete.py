
# Andrew Schaefer
# 6/22/21
# CSD310 Mod 6.2 (b)
 
# Imports Pymongo tools
import pymongo 

# Connects to MongoDB database
myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.zcfrz.mongodb.net/pytech?retryWrites=true&w=majority")
mydb = myclient["pytech"]
mycol = mydb["students"]

# Finds all pytech.students documents and displays them
x = mycol.find()
print(list(x))

# Inserts and displays a new document 
data_1 = [{
    "student_id" : 1010, "first_name" : "Frank", "last_name" : "Sinatra"
}]
x = mycol.insert_many(data_1)
print(x.inserted_ids)

# Finds and displays newly inserted document
y = mycol.find_one({"student_id": 1010})
print(y)

# Deletes document
z = mycol.delete_one({"student_id": 1010})

# Finds all pytech.students documents and displays them
x = mycol.find()
print(list(x))