
num = int(input("Enter a number: "))
count = 0

if num <= 1:
    print("The number is not  prime")
else:
    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count == 0:
        print("The number is prime")
    else:
        print("The number is not prime")


for i in range(14):
    if i==6:
        break
    print("value of i from break:",i)
else:
    print("value of i from continue:",i)
