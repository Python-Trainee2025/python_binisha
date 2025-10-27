contact_info = {'Ram': 9811111111, 'Sita': 9822222222, 'Hari': 9833333333}

name = input("Enter a name you want to search: ")

if name in contact_info:
    print(f"Name is {name} and contact info is {contact_info[name]}")
else:
    print("Sorry that name is not in contact info.")