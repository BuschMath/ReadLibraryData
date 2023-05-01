import csv

filename = "Final_LibraryBookData.csv"
data = []

with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

print(data)
