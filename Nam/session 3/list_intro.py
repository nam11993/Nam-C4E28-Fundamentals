# menu = ["Com","Bun","Pho","Thit","Rau"]

# menu.append("Banh Cuon")

# print(*menu, sep=", ")

# fav = ["da bong","game","nhac"]
# for index in range(len(fav)):
#     print fav[index]

# n = input("nhap them so thich: ")

# fav.append(n)

# print(*fav, sep=", ")


#loop with item
menu = ["Com","Bun","Pho","Thit","Rau"]
# for item in menu:
#     print(item)

#loop with index
# for index in range(len(menu)):
#     print(index, menu[index], sep=". ")

# #loop with item, index
# for index, item in enumerate(menu):
#     print(index+1, item, sep=". ")

# #update
# menu[0] = "Chao"
# print(menu)


# favorite = ["death note","netflix","teching"]
# print(favorite)
# for index, item in enumerate(favorite):
#     print(index+1, item, sep=". ")

# n = int(input("Position you want to update: "))
# m = input("Your replacing favorite? ")

# favorite[n-1] = m
# for index, item in enumerate(favorite):
#     print(index+1, item, sep=". ")


#delete
# menu.pop(1)
# del menu[2]

# print(*menu, sep=", ")


favorite = ["death note","netflix","teching"]
for index, item in enumerate(favorite):
    print(index+1, item, sep=". ")

position = int(input("Favorite position you want to get rid of: "))

del favorite[position-1]

for index, item in enumerate(favorite):
    print(index+1, item, sep=". ")
