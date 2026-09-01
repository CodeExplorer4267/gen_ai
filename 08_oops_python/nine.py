#Property decorator 
class Student:
    # marks=70
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s=Student("Rupam",68)
# print(s.marks) #68
# s.marks=90
# print(s.marks)#90
# print(Student.marks)#70
#but we can change the value into some invalid value

class Student:
    # marks=70
    def __init__(self,marks):
        self._marks=marks

    @property #controls how the value is read
    def marks(self):
        return self._marks
        # if(self._marks > 100 or self._marks < 0):
        #     return "Invalid Input"
        # else:
        #     return self._marks
    
    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks")



# s=Student(90)
# print(s.marks) #90
s=Student(900) 
# print(s.marks) #Invalid input  
s.marks=101
print(s.marks)
# looks like an ordinary variable.
# But internally Python is actually calling:
# marks()
