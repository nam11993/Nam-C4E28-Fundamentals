# yob = int(input("enter you yob? "))
# age = 2019 - yob
# print(age)

# if age < 10:
#     print("Baby")
# elif age < 18: 
#     print("Teenager")
# else:
#     print("not baby")


# from random import randint

# x = randint(0, 100)
# print(x)
# if x < 36:
#     print("Sunny")
# elif x < 71:
#     print("Rainy")
# else:
#     print("Cloudy")

# a = randint(1,10)
# print(a)
# b = randint(1,10)
# print(b)
# c = randint(1,10)
# print(c)
# kq = b**2 - (4 * a * c)
# print(kq)
# if kq < 0:
#     print("vo nghiem")
# elif kq == 0:
#     print("nghiem kep")
# else:
#     print("co 2 nghiem phan biet")
#     x1 = (-b + delta**0.5)/(2*a)
#     x2 = (-b + delta**0.5)/(2*a) 
#     print(x1,x2)

n = int(input("nhap n:"))
m = int(input("nhap m:"))

for i in range(n, m+1):
    if (i % 2 == 0):
        print(i)