while True:
    ques = {
        1: 35,
        2: 36,
        3: 40,
        4: 44
    }
    print('''
Anwer the following algebra question:
If x = 8, then what is the value of 4(x+3) ?''')
    for index, item in enumerate(ques):
        print(index+1, item, sep='. ')

    your_choice = int(input("Your choice: "))

    if your_choice == 4:
        print("Bingo")
        break
    elif your_choice > 4:
        print("cu phap khong hop le")
    else:
        print(':(')