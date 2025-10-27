Word1=str(input("Enter a  word: ").lower())
Word2=str(input("Enter another word: ").lower())

if sorted(Word1)==sorted(Word2):
    print("Words are anagram")
else:
    print("Words are not anagram")
