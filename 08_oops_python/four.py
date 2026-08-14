#create two students with name and marks. delete student 1's marks and change to class's marks. A and B te attribute add kore "present or not " print

class Student:
    name=""
    marks=5
    def __init__(self,name="No Name",marks="0"):
        self.name=name
        self.marks=marks

    def is_present(self):
        return f"{self.name} is {self.is_Present}"

stu1=Student("Rupam",45)
stu2=Student("Sam",83)
# print(stu1.is_present("Not present"))
# print(stu2.is_present(" present"))

# del stu1.marks #attribute shadowing
# print(stu1.marks)

stu1.is_Present="Present"
stu2.is_Present=False

print(stu1.is_present()) #Rupam is Present

