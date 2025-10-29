def vowel_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1

    print(f"The number of vowels is: {count}")
sentence=input("Enter a word or sentence: ").lower()
vowel_count(sentence)


