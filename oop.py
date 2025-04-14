class Book:
    def __init__(self,title, author,pages, yearofpublication,genre):
        self.title = title
        self.author = author
        self.yearofpublication = yearofpublication
        self.genre = genre
        self.pages = pages

    def borrowBook(self):
        print("You have borrowed the book:", self.title)

    def returnBook(self):
        print("You have returned the book:", self.title)

    def isLong(self):
        if self.pages > 300:
            print("This is a long book.")
        else:
            print("This is a short book.")

    def displayBookInfo(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year of Publication:", self.yearofpublication)
        print("Genre:", self.genre)


book1=Book("The Alchemist","Paulo Coelho",208,1988,"fiction")
book2=Book("Rich Dad Poor Dad","Robert Kiyosaki",336,1997,"self-help")
book3=Book("The art of not giving a f*ck","Mark Manson",224,2016,"self-help")

book1.displayBookInfo()  
book2.displayBookInfo()
book3.displayBookInfo()

book1.borrowBook()

#polymorphism
class Car:
    def move(self):
        print("Driving a car")
class Bicycle:
    def move(self):
        print("Riding a bicycle")           
class Plane:
    def move(self):
        print("Flying a plane")

def make_it_move(entity):
    entity.move()

# Create objects
my_car = Car()
my_plane = Plane()
my_bicycle = Bicycle()  

make_it_move(my_car)
make_it_move(my_plane)
make_it_move(my_bicycle)