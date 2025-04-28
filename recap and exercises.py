# Instance Variables



class Dog:
    def __init__(self, name):
        self.name = name  # instance variable
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name)  # Buddy
print(dog2.name)  # Max
