import csv
import xml.dom.minidom

count = 0
with open("books.csv") as file:
    books = csv.reader(file, delimiter=";")
    next(books)
    for book in books:
        if len(book[1]) > 30:
            count += 1

print("Количество записей:", count)



author = input("Введите автора: ").lower()

with open("books.csv") as file:
    books = csv.reader(file, delimiter=";")
    next(books)
    for book in books:
        if author in book[3].lower():
            print(book[3], "-", book[1])



with open("books.csv") as file:
    books = csv.reader(file, delimiter=";")
    next(books)
    with open("result.txt", "w") as result:
        for number in range(1, 21):
            book = next(books)
            year = book[6][6:10]
            result.write(f"{number}. {book[3]}. {book[1]} - {year}\n")

print("result.txt")



document = xml.dom.minidom.parse("currency.xml")
char_codes = []
values = []

for code in document.getElementsByTagName("CharCode"):
    char_codes.append(code.firstChild.data)

for value in document.getElementsByTagName("Value"):
    values.append(value.firstChild.data)

print("CharCode:", char_codes)
print("Value:", values)
