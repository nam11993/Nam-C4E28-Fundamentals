from random import choice
many_word = ["champion","dungeon","homework"]
word = choice(many_word)
random_list = []
list_word = list(word)

while len(list_word) > 0:
    char = choice(list_word)
    random_list.append(char)
    list_word.remove(char)

print(*random_list, sep=" ")
while True:
    user_word = input("your answer: ")
    if user_word == word:
        print("hura")
        break
    else:
        print(":(")