#title: gonzalez_usersp2.py
#author: Janis Gonzalez
#date: 04/30/2023
#description: python and mongodb

# import MongoClient
from pymongo import MongoClient
import datetime

# build a connection string 
client = MongoClient('mongodb+srv://web335_user:s3cret@web335db.jv4wnqk.mongodb.net/web335DBretryWrites=true&w=majority')

print(client)

# configure a variable to access web335DB
db = client['web335DB']

#create new user document by assigning fields to a variable
janis = {
    "firstName": "Janis",
    "lastName": "Gonzalez",
    "employeeId": "1445",
    "email": "janis@me.com",
    "dateCreated": datetime.datetime.now()
}

#inserts the document into the users collection
janis_user_id = db.users.insert_one(janis).inserted_id
print(janis_user_id)

#prove the insert worked
print(db.users.find_one({"employeeId": "1445"}))

#creates an update query to change the user's email address
db.users.update_one(
    {"employeeId": "1445"},
    {
        "$set": {
            "email":"janisnew@me.com"
        }
    }
)

#prove email was updated
print(db.users.find_one({"employeeId": "1445"}))


#builds a query to remove user document
result = db.users.delete_one({
    "employeeId": "1445"
})

#display the result of the query
print(result)

#prove the delete
print(db.users.find_one({"employeeId": "1445"}))