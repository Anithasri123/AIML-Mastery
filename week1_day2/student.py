class Student:
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks 
    def display(self):
        print(f"Name : {self.name}")
        print(f"Marks : {self.marks}")
    def calculate_grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=70:
            return "B"
        elif self.marks>=50:
            return "C"
        else:
            return "Fail"
s1=Student("Ani",50)
s1.display()
grade=s1.calculate_grade()
print(f"Grade of {s1.name} is {grade}")
        
            