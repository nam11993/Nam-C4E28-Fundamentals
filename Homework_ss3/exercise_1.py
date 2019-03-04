quanao = ["T_Shirt", "Sweater"]
while True:   
    R = input("Welcome to our Shop, what do you want (C, R, U, D)? ")
    if R == "R":
        print("Our items: ", end="")
        print(*quanao, sep=", ")

    elif R == "C":
        creat = input("New item? ")
        quanao.append(creat)
        print("Our items: ", end="")
        print(*quanao, sep=", ")

    elif R == "U":
        up = int(input("Update Position? "))
        ui = input("New item? ")
        quanao[up-1] = ui
        print("Our items: ", end="")
        print(*quanao, sep=", ")   

    elif R == "D":
        i = int(input("Delete Position? "))
        del quanao[i-1]
        print("Our items: ", end="")
        print(*quanao, sep=", ")
        break