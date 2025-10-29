#input income amount and tax rate in one line, calculate total as income*tax and display
i=list(map(int,input("Enter value for income amount and tax rate:").split(" ")))
total=i[0]*i[1]
print(f"Total is {total}")

