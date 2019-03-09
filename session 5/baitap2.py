x = int(input("Input x: "))
y = int(input("Input y: "))
# result = x + y
# print("sum x + y =",(result))
op = input("input op: ")

result = 0
if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x / y

print(result)
