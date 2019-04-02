from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e28-s3lzu.mongodb.net/test?retryWrites=true"
client = MongoClient()
db = client.db_service
bikes = db["bike"]
