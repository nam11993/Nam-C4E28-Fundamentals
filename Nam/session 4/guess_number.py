print('''
Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' id my guess is 'S'maller than your number
'l' id my guess is 'L'arger than your number
''')

low = 1
high = 101

while True:
    mid = (low+high) // 2
    answer_input = input("Is {0} your number? ".format(mid))
    if answer_input == "c":
        print("I knew it")
        break
    elif answer_input == "l":
        high = mid
    elif answer_input == "s":
        low = mid

