class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"'{self.title}' by {self.author}")

book1 = Book("The Alchemist", "Paulo Coelho")

print("Title: ", book1.title)
print("Author: ", book1.author)
book1.display_info()