class Movie:
    def __init__(self, title,year):
        self.title = title
        self.year = year

    def __eq__(self, other):
        return self.year == other.year
    
    def __lt__(self, other):
        return self.year < other.year
    

movie1 = Movie("Inception", 2010)
movie2 = Movie("The Matrix", 1999)

print(movie1 == movie2)
print(movie1 < movie2)
print(movie2<movie1)