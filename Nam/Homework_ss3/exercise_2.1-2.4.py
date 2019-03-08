#2.1
size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and these are my sheeps size")
print(size)

#2.2
print("Now my biggest sheep has size", max(size), end="")
print(" let's shear it")

#2.3
i = size.index(max(size))
size[i] = 8
print("After shearing, here is my flock")
print(size)

#2.4
for i in range(7):
    size[i] = size[i] +50
print("One month has passed, now here is my flock")
print(size)