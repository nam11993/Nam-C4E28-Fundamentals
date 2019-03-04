#2.6
size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and here is my flock")
print(size)

print("Now my biggest sheep has size", max(size), end="")
print(" let's shear it")

i = size.index(max(size))
size[i] = 8
print("After shearing, here is my flock")
print(size)

print("MONTH 1: ")
for i in range(7):
    size[i] = size[i] +50
print("One month has passed, now here is my flock")
print(size)

print("Now my biggest sheep has size", max(size), end="")
print(" let's shear it")

i = size.index(max(size))
size[i] = 8
print("After shearing, here is my flock")
print(size)

print("MONTH 2: ")
for i in range(7):
    size[i] = size[i] +50
print("One month has passed, now here is my flock")
print(size)

print("Now my biggest sheep has size", max(size), end="")
print(" let's shear it")

i = size.index(max(size))
size[i] = 8
print("After shearing, here is my flock")
print(size)

print("MONTH 3: ")
for i in range(7):
    size[i] = size[i] +50
print("One month has passed, now here is my flock")
print(size)


total = sum(size)
money = total*2
print()
print("My flock has size in total: ", total)
print("I would get", total, "* 2$ = ", money, "$")
