class Student:
    def __init__(self,name):
        self.name = name
        self.__grades = []

    def add_grade(self,grade):
        self.__grades.append(grade)
    
    def get_average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0
    
s = Student("Amina")
s.add_grade(85)
s.add_grade(90)
s.add_grade(95)

print(s.get_average())
