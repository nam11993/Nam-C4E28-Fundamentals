dict = {
    "hc": "hoc",
    "eny": "em nguoi yeu",
    "any": "anh nguoi yeu",
    "lm": "lam"
}
while True:
    print(*dict.keys())
    i = input("Letter do you want translate: ")
    if i in dict.keys():
        letter = dict[i]
        print((i),(letter), sep =": ")
    else:
        j = input("no letter you search, what do you want contribute? (y-n): ").lower()
        if j == "y":
            n = ("do you want translate? ")
            dict[i] = n
        elif j == "n":
            break
