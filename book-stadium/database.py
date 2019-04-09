from pymongo import MongoClient

mongo_uri = 'mongodb+srv://admin:admin@c4e28-s3lzu.mongodb.net/test?retryWrites=true'

client = MongoClient(mongo_uri)

service_database = client.db_service

stadiums = service_database["stadiums"]

sanbong = [
    {
        "id": 1.2,	
        "district":	'Hai Bà Trưng',
        'name':	"Trường ĐH Bách Khoa",
        'address': '123abc', 	
        'time':	'4h00',
        'contact': 'Sân bóng trường ĐH Bách Khoa - 0438680186',	
        'description': 'Sân bóng Nguyễn An Ninh là sân cỏ nhân tạo với diện tích rộng.', 
    },
    {
        "id": 1.2,	
        "district":	'Hai Bà Trưng',
        'name':	"Trường ĐH Bách Khoa",
        'address': '123abc', 	
        'time':	'8h00',
        'contact': 'Sân bóng trường ĐH Bách Khoa - 0438680186',	
        'description': 'Sân bóng Nguyễn An Ninh là sân cỏ nhân tạo với diện tích rộng.', 
    }
]