
def count_words(file_name):
    try:
        with open(file_name,'r') as file:
            content =file.read()
            words=content.split()
            print(f"Number of words in {file_name}: {len(words)}")
    except FileNotFoundError:
        print(f"File {file_name} not found")
file_name=input("Enter the filename: ")
count_words(file_name)