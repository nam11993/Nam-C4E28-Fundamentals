from turtle import *
#1
# def hello_world():
#     for i in range(3):
#         print("Hello World")
# hello_world()

#2
# def number(x,y):
#     sum = x + y
#     print(sum)
# number(5,4)

#3
# def draw_square(length,colorr):
#     color(colorr)
#     for i in range(4):
#         forward(length)
#         left(90)
# draw_square(100,"red")
#4
# for i in range(30):
#     draw_square(i * 5, 'red')
#     left(17)
#     penup()
#     forward(i * 2)
#     pendown()

#5
def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        right(144)
        forward(length)
# draw_star(-100,10,100)
#6
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()