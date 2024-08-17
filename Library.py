class Books:
    def __init__(self,Title,Author,ISBN):
        self.__Title=Title
        self.__Author=Author
        self.__ISBN=ISBN

    def Book_Info(self):
        print(f"The Book is {self.__Title} by {self.__Author} .\nIts ISBN No. is {self.__ISBN}")

    def get_BookInfo(self):
        return self.__Title,self.__Author,self.__ISBN
    
    def set_BookInfo(self,Title,Author,ISBN):
        self.__Title=Title
        self.__Author=Author
        self.__ISBN=ISBN

class User:
    def __init__(self,Name,userID):
        self.__Name=Name
        self.__userID=userID
        self.__Borrowed_Books=[]

    def User_Info(self):
        print(f"User Name :- {self.__Name}\nUserID :- {self.__userID}\nNo. of Borrowed Books :- {self.__Borrowed_Books}")

    def BorrowBook(self):
        print(f"Borrowing Book {self.__Borrowed_Books}")    
        
    def get_UserInfo(self):
        return self.__Name,self.__userID,self.__Borrowed_Books
    
    def set_UserInfo(self,Name,userID):
        self.__Name=Name
        self.__userID=userID
    
    def add_Borrowed_Books(self,book):
        self.__Borrowed_Books.append(book)
    
    def remove_Borrowed_Books(self,book):
        if book in self.__Borrowed_Books:
            self.__Borrowed_Books.remove(book)
        else:
            print("Book not found in the Borrowed List.")

class Library_User(User):
    def __init__(self, Name, userID,Membership_Level):
        super().__init__(Name,userID)
        self.__Membership_Level=Membership_Level
    def BorrowBook(self):
        if self.__Membership_Level=="Premium":
            print("Borrowing Premium Subscription Books")
        elif self.__Membership_Level=="Gold":
            print("Borrowing Gold Subscription Books")
        else:
            print("Borrowing Normal Subscription Books")
    
print ("Hello")