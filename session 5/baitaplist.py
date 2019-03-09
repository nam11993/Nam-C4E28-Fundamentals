info = [
    {
        "name": "quan",
        "sph": 25,
        "hour": 3,
        "day": 20
    },
    {
        "name": "duc",
        "sph": 80,
        "hour": 5,
        "day": 15
    }
]
# name = input("input name: ")
# salary = 0
# for each_name in info:
#     found = False
#     if name == each_name["name"]:
#         salary = each_name["sph"] * each_name["hour"] * each_name["day"]
#         found = True
#         break
#     else:
#         found = False

#     if found:
#         print(salary)
#     else:
#         print("Not found")

total_salary = 0
for each_name in info:
    total_salary += each_name["sph"] * each_name["hour"] * each_name["day"]

print(total_salary)


