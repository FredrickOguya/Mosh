class Movie:
    def __init__(self,title,year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"
    
movie = Movie("Inception", 2010)
print(movie)