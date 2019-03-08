# username = "c4e"
# password = "codethechange"
# loop = True
# count = 0
# while loop:
#     name = input("enter your username: ")
#     passw = input("enter your password: ")
#     if name == username and passw != password:
#         print("sai pass")
#         count = count + 1
#         if count == 3:
#             loop = False
#     elif name != username:
#         print("khong tim thay user")
#         break

#     else:
#         print("welcome")
#         break

username = "c4e"
password = "codethechange"
count = 0
user_input = input("username: ")

loop = True
while loop:
    if user_input == username:
        password_input = input("password: ")
        if password_input == password:
            print("welcome")
            loop = False
        else:
            print("wrong password")
            print("try again pass")
            count += 1
            if count == 3:
                loop = False
    else:
        print("User not found")
        loop = False
