#Solution made by me.

class Library:
    books = ['Science','Maths','SSt','Marathi','Hindi','English']
    num_of_books = len(books)

l1 = Library()
i = 0
n = 1
print("How many books you want to enter?")
i = int(input())
while(n<=i):
    print(f"Enter name of book number {n}: ")
    book = input()
    l1.books.append(f"{book}")
    n = n + 1

print(f"Now the library has {len(l1.books)} books.")
print("The edited list of books is: ")
print(l1.books)    


#Official solution given by CodeWithHarry

# class Library:
#   def __init__(self):
#     self.noBooks = 0
#     self.books = []
    
#   def addBook(self, book):
#     self.books.append(book)
#     self.noBooks = len(self.books)

#   def showInfo(self):
#     print(f"The library has {self.noBooks} books. The books are")
#     for book in self.books:
#       print(book)


# l1 = Library()
# l1.addBook("Harry Potter1")
# l1.addBook("Harry Potter2")
# l1.addBook("Harry Potter3")
# l1.showInfo()