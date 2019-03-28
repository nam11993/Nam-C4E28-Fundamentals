import ex4

db = ex4.connect()
rivers = db["river"]

rivers_s_america = rivers.find({'continent': 'S. America'})

for i in rivers_s_america:
    if i["length"] < 1000 :
        print(i["name"],":",i["length"],"km")