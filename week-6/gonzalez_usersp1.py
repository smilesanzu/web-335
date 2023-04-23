#title: gonzalez_usersp1.py
#author: Janis Gonzalez
#date: 04/23/2023
#description: python and mongodb

# import MongoClient
from pymongo import MongoClient

# build a connection string 
client = MongoClient('mongodb+srv://web335_user:s3cret@web335db.jv4wnqk.mongodb.net/web335DBretryWrites=true&w=majority')

print(client)

# configure a variable to access web335DB
db = client['web335DB']


# display all documents in the user’s collection
print('List all documents in collection.')

for user in db.users.find():

    print(user)


# display a document where the employeeId is 1011
print('Display employee 1011.')

print(db.users.find_one({'employeeId': '1011'}))


# display a document where the lastName is Mozart
print('Display user with the lastName Mozart.')

print(db.users.find_one({'lastName': 'Mozart'}))