def name():
    print("My name is Anna")
name()

def name(naam):
    print(f"My name is {naam}")
name("Ram")

#passing arguments
def add(a,b):
    print("sum is :",a+b)
add(2,5)

#default arguments
def sub(c=9,d=4):
    print("sub is :",c-d)
sub(2)

#named arguments
def add(*args):
    total=0
    for num in args:
        total+=num
    return total
add(1,2,6,7)

#keyword arguments
def info(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
info(name="Ram",gender="male",age=20)


