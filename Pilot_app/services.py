from pymongo import MongoClient
from faker import Faker
from random import randint, choice
from bson.objectid import ObjectId

faker = Faker()

mongo_uri = "mongodb+srv://admin:admin@c4e28-s3lzu.mongodb.net/test?retryWrites=true"

#1 Connect to cluster
client = MongoClient(mongo_uri)

#2 Get/ Create Database
service_database = client.db_service

#3 Get/ Creat collection
services = service_database["services"]

#4 Create document, insert document
# for i in range(50):
#     new_service = {
#         "name": faker.name(),
#         "age" : randint(18,30),
#         "address" : faker.address(),
#         "gender" : choice(["male", "female"]),
#         "available" : choice([True, False]),
#     }
#     services.insert_one(new_service)
#     print("Saving document {0} .... ".format(i+1))

#5 Read 
#5.1 Read all
# all_services = services.find() #lazy loading
# print(all_services) #same list
# print(all_services[0])
# for service in all_services:
#     print(service["name"])

#5.2 Read only one
# one_service = services.find_one({"name" : "Justin Bird"})
# one_service = services.find_one({"_id": ObjectId('5c9a1d75bc2d4c3bace02136') })
# print(one_service)

#6 delete
# service = services.find_one({ "_id": ObjectId('5c9a1d75bc2d4c3bace02136') })
# if service is not None:
#     services.delete_one(service)
# else:
    # print("Not found document!")
# print(service)


#7 Update
one_service = services.find_one({ "_id": ObjectId('5c9a1d76bc2d4c3bace0213a') })
new_value = { "$set": { "gender": "female"} }
services.update_one(one_service, new_value)
print(one_service)