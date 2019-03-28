from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client=MongoClient(mongo_uri)
db=client.c4e
customers = db.customers.find()

events = 0
ads = 0
wom = 0
for i in customers:
    if i['ref'] == "events":
        events += 1
    elif i['ref'] == "ads":
        ads += 1
    elif i['ref'] == "wom":
        wom += 1
total = events + ads + wom

print("Customers of events :",events)
print("Customers of wom :", wom)
print("Customers of ads :",ads)

ref_data = [events, ads, wom]
ref_name = ["events", "advertisements", "word of mouth"]
pyplot.pie(ref_data, labels=ref_name, autopct="%.1f%%", shadow=True, explode=[0, 0.05, 0.05])
pyplot.title("References")
pyplot.axis("equal")
pyplot.show()
