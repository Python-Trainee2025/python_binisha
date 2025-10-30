import csv
file= input("Enter the csv filename: ")

try:
  with open(file,'r') as file:
      reader = csv.reader(file)
      for row in reader:
          print(row)

except FileNotFoundError:
    print("CSV file not found")
except csv.Error as e:
    print(f"CSV error: {e}")