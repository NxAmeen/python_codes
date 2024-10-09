class book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year

    def getBookInfo(self):
        return f'Title : {self.title}\n Author : {self.author}\n Year : {self.year}'
    

title=input('Enter the title of the book: ')
author=input('Enter the author of the book: ')
year=input('Enter the year of publication: ')

book=book(title,author,year)

print(book.getBookInfo())