class LMS:
    def __init__(self):
        self.books={}
    def add_books(self,book,quantity):
        if book in self.books:
            self.books[book]+=quantity
            print(f"{book} is added")
        else :
            self.books[book]=quantity
    def issue_books(self,book):
        if book in self.books and self.books[book]>0:
            self.books[book]-=1
            print(f"{book} issued successfully")
        else:
            print("Book is not available")
    def return_books(self,book):
        self.books[book]+=1
        print(f"{book} is returned")
    def display(self):
        print("Available books are:")
        for book,count in self.books.items():
            print(f"{book} : {count}")

p1=LMS()
p1.add_books("CNS",2)
p1.add_books("CNAP",3)
p1.issue_books("CNAP")
#p1.return_books("CNAP")
p1.display()
        
        