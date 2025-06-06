class Library():
    def __init__(self,bookList):
        self.booklist = bookList

    def displayBook(self):
        for i in range(len(self.booklist)):
            print(f"{i+1}.", self.booklist[i])
        
    
    def borrowBook(self,book):
        if book in self.booklist:
            self.booklist.remove(book)
            print(f"You borrowed the book {book}. Return in 30 days.")
        else:
            print("Book not aviailble")
    
    def returnBook(self,book):
        self.booklist.append(book)
        print(f"You successfully deposited the book {book}")
        

class Student():
    def borrowBook(self):
        book = input("Enter book you want to borrow : ")
        return book
        
    def returnBook(self):
        book = input("Enter book you want to deposit : ")
        return book
    
if __name__ == "__main__":
    
    klib = Library(["a","b","c"])
    krishna = Student()
        
    while True:
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        option = input()
        print("")
        
        if option == "1":
            klib.displayBook()
            
        if option == "2":
            
            klib.borrowBook(krishna.borrowBook())
        if option == "3":
            klib.returnBook(krishna.returnBook())
        if option == "4":
            exit()