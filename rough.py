class a:
    def __init__(self,book1):
        print(book1)
    def b(self,book):
        self.book=book
        print(self.book)
        print(book)
    
c=a("hi")
c.b("harrypoter")