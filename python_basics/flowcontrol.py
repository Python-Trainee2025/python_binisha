#for loop
l=[1,2,3,4,5]
for num in l:
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#range
for i in range(1,10,2):
    print(i)


#while loop
c=0
while c<10:
    print(c)
    c+=2

#break
#pass :placeholder statement
#continue

#pass
for i in range(5):
    if i==4:
        pass
    print("value of i from pass:",i)


#break
for i in range(5):
    if i==4:
        break
    print("value of i from break:",i)

#continue
for i in range(5):
    if i==4:
        continue
    print("value of i from continue:",i)





