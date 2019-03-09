from random import randint
from random import choice
# from calc import eval
import calc

while True:
    x = randint(0,10)
    y = randint(0,10)
    op = choice(["+","-","*","/"])

    errors = randint(-1,1)

    real_result = calc.eval(x, y, op)
    
    display_result = errors + real_result
    
    print("{0} {1} {2} = {3}".format(x, op, y, display_result))
    user_input = input("Y/N: ").lower()

    if user_input == "y":
        if errors == 0:
            print("yura")
        else:
            print("You're wrong")
            break
    elif user_input == "n":
        if errors == 0:
            print("You're wrong")
            break
        else:
            print("yura")
    else:
        break



