import mongodb

database = mongodb.connect()

collection = database["posts"]