class Library:
    def __init__(self,noofBooks):
        self.Book=[]
        self.noofBooks=0
    
    def add_Books(self,Title):
        self.Book.append(Title)#Title was used here cause if we use self.title it will just add the default value
        self.noofBooks=len(self.Book)
        print(f"{Title} added. Total No. of Books is {self.noofBooks}")

    def remove_Books(self,Title):
        if Title in self.Book:
            self.Book.remove(Title)#Title was used here cause if we use self.title it will just add the default value
            self.noofBooks=len(self.Book)
            print(f"{Title} removed. Total No. of Books is {self.noofBooks}")

    def check_books(self):
        if self.noofBooks==len(self.Book):
            print("Both are Same")
        else:
            raise ValueError("They dont Match.")

a=Library(2)
a.add_Books("Tom Gates"
            )
# a.remove_Books("Germino Stiltion")
# a.check_books()
