word=input("Enter  a word to check if it is palindrome or not?: ").lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")