
ques1 = {
    1: 35,
    2: 36,
    3: 40,
    4: 44
}

ques2 = {
    1: "About 55",
    2: "About 65",
    3: "About 75",
    4: "About 85"
}

count = 0

while True:
    print('''Question 1: Answer the following algebra question:
If x = 8, then what is the value of 4(x+3)?''')

    for i, j in ques1.items():
        print(i, j, sep='. ')

    your_choice1 = int(input("Your choice(1-4): "))

    if your_choice1 == 4:
        print("Bingo")
        count += 1
    elif 1 > your_choice1 or your_choice1 > 4:
        print("Invalid syntax")
    else:
        print(':(')

    print('''Question 2: Estimate this answer (exact caculation not needed):
Jack scored these marks in 5 math test: 49, 81, 72, 66 and 52. What is the mean?''')
    for x, y in ques2.items():
        print(x, y, sep='. ') 
        
    your_choice2 = int(input("Your choice(1-4): "))

    if your_choice2 == 2:
        print("Bingo")
        count += 1
        break
    elif 1 > your_choice2 or your_choice2 > 4:
        print("Invalid syntax")
        break
    else:
        print(':(')
        break

print("*******************")
print("You correctly answer {} out of 2 questions".format(count))
