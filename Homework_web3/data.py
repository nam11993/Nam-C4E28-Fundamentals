from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@c4e28-s3lzu.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
db = client.db_service
bikes = db["bike"]
