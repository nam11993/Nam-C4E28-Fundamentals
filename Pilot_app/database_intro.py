from pymongo import MongoClient

mongo_uri ="mongodb+srv://admin:admin@pilot-app-svez3.mongodb.net/test?retryWrites=true"

#1. connect to database
client = MongoClient(mongo_uri)

#2 Get database
db = client.test

#3 Create collection
games = db["games"]

#4 Create document
new_game = {
    "name": "Pikachu",
    "description": "Alway lost money",
}

#5. insert document
games.insert_one(new_game)