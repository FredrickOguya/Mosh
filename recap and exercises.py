class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name}, I'm {self.age} years old.")

class Student(Person):
    
    def __init__(self,name, age, school):
        super().__init__(name,age)
        self.school = school
    
    def introduce(self):
        super().introduce()
        print(f"I study at {self.school}")