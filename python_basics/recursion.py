def fact(num):
    res=1
    for i in range(2,num-1):
        res=res*i
    return res
print(fact(9))

def fact(num):
    if num==1:
        return 1
    return num*fact(num-1)
print(fact(5))

def sq(num):
    return num*num
print("sQUARE IS: ",sq(5))

#lambda function
sq=lambda num: num*num
print("Square of a number is: " ,sq(9))

max= lambda a,b: a if a>b else b
print("Maximum number is: ",max(1,3))
