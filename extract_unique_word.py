import string

sentence=str(input("Enter a sentence or paragraph: ").lower())

i = sentence.translate(str.maketrans('', '', string.punctuation))

words=i.split()

unique_words=set(words)

print(f"The unique words are: {unique_words} and their count is: {len(unique_words)}")
