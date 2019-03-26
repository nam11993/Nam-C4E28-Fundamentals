from model import collection


new_post = {
    "title": "C4E28",
    "author": "Nam Nguyễn",
    "content": "Hello, say goodbye",
}

collection.insert_one(new_post)
