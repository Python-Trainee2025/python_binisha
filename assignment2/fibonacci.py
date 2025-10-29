num = int(input("Enter a number: "))
a, b = 0, 1
i = 0
print("Fibonacci sequence: ")
while i < num:
    print(a)
    a, b = b, a + b
    i += 1

#recursive method
def fibonacci_recursive(n):
    if n<=1:
        return n
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
print("\nFibonacci sequence(Recursive): ")
for i in range(num):
    print(fibonacci_recursive(i),end=" ")


