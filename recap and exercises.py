class Student:
    school_name = "Greenwood High"
    def __init__(self,name,grade):
        self.name= name
        self.grade = grade
    def display_info(self):
        print(f"Name: {Student.name}")
        print(f"Grade: {Student.grade}")
        print(f"School: {Student.school_name}")