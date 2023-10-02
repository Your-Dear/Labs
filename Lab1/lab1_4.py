from csv import reader
from datetime import datetime
import random

with open("books.csv", encoding="cp1251") as csv_books:
    
    file = reader(csv_books,delimiter=";")
    books = list(file)
    books = books[1:]
    
    # 1°
    num_lines= len(books)
    print("Number of books: ", num_lines)
    
    # 2°
    a=0
    for book in books:
        lenght= len(book[1])
        if lenght>30:
            a+=1
    print("\nQuantity of books with more than 30 characters: ", a)
    
    # 3°
    given_author = input("\nName of the author: ")
    count = 0
    for book in books:
        
        book_name = book[1]
        author = book[3]
        date = book[6]
        
        # 13.01.2017 16:24
        dateTimeObj = datetime.strptime(date, "%d.%m.%Y %H:%M")
        year = dateTimeObj.year
        
        # if year in [2014, 2016, 2017]:
        if year == 2014 or year == 2016 or year == 2017:
            if author == given_author:
                count += 1
                print(f"{count}/. {author} - {book_name}")

    # 4°    
    count = 0
    result = ""
    random_books = random.choices(books,k=20)
    
    for book in random_books:
        count+=1
        date = book[6]
        dateTimeObj = datetime.strptime(date, "%d.%m.%Y %H:%M")
        year = dateTimeObj.year
        author = book[3]
        name = book[1]
        
        result += f"{count}/. {author}. {name} - {year}\n"
    
    print("\nCite generator of random books:")
    print(result)
    
    with open("generator.txt", "w", encoding="cp1251") as generator:
                
        generator.write(result)


    print("\n\nDop Zadanye\n\n")


    # dop 1

    tags = {}
    for book in books:
        book_tags = book[12].split("#")
        for tag in book_tags:
            if(tag):
                tags[tag.strip()] = True
                
    with open("tags.txt", "w", encoding="cp1251") as tag_file:
        result = ""
        for tag in tags.keys():
            result += tag + "\n"
        tag_file.write(result)
    
    print("Tags are in tags.txt!!\n")
    
    # dop 2

    top_books = sorted(books, key=lambda d: int(d[8]), reverse=True)
    for i in range(20):
        book = top_books[i]
        print(f"{i + 1}/. {book[1]} - {book[8]}")