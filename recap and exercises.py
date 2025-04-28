class Dog:
    species = "Canine"
    def __init__(self,name,breed):
        self.name= name
        self.breed = breed
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")

dog1 = Dog("Buddy", "Labrador")
dog1.display_info()