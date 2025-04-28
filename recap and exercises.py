class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __add__(self, other):
        return self.duration + other.duration
    
m1 = Movie("Inception", 148)
m2 = Movie("Intersteallar", 169)

print(m1 + m2)