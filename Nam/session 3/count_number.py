n = input("enter number: ")

count = 0
while n > 0:
    n = n // 10
    count += 1
    print(n)
print(count)

# count = len(n)
# print(count)