num = int(input("enter a number: "))

is_prime = True
i = 2

if num == 0 or num == 1:
    is_prime = False
else:
    # for i in range(2,num):
    #     if num % i == 0:
    #         is_prime = False
    #         break
    # if is_prime == True:
    #     print("snt")
    # else:
    #     print("ko phai so nt")

    while i < n:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime == True:
        print("snt")
    else:
        print("ko phai so nt")
