#3.a
import random
# char = ["c","h","a","m","p","i","o","n"]
# i = random.shuffle(char)
# word = "champion"
# print(*char)
# while True:
#     g = input("Your answer: ")
#     if g != word:
#         print(":(")
#     else:
#         print("Hura")
#         break

#3.b
list1 = ["m","e","t","i","c","u","l","o","u","s"]
list2 = ["c","h","a","m","p","i","o","n"]
list3 = ["h","e","x","a","g","o","n"]

word1 = "meticulous"
word2 = "champion"
word3 = "hexagon"

count = 0
        
while True:
    if(count == 0):
        i = random.shuffle(list1)
        print("Question1:", *list1)
        g = input("Your answer: ")
        if g != word1:
            print(":(")
        else:
            count = count+1
            print("Hura")

    elif(count == 1):
        i = random.shuffle(list2)
        print("Question2:", *list2)
        g = input("Your answer: ")
        if g != word2:
            print(":(")
        else:
            count = count+1
            print("Hura")

    elif(count == 2):
        i = random.shuffle(list3)
        print("Question3:" , *list3)
        g = input("Your answer: ")
        if g != word3:
            print(":(")
        else:
            count = count+1
            print("Hura")
    
    else:
        break
