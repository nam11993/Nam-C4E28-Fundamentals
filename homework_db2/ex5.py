import ex4

db = ex4.connect()
rivers = db["river"]

rivers_africa = rivers.find({'continent': 'Africa'})
for i in rivers_africa:
    print(i["name"],":",i["length"],"km")
