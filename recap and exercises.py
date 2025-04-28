class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __len__(self):
        return self.age
    
cat = Cat("whiskers", 5)
print(len(cat))
    