class Person:
  def __init__(self, student, prelim, midterm, finals):
    self.__student = student
    self.__prelim = prelim
    self.__midterm = midterm
    self.__finals = finals

  def grades(self):
    return (self.__prelim + self.__midterm + self.__finals)/3

  def display(self):
   print(f"This student is {self.__student}\n ")
   print(f"Prelim Grade: {self.__prelim}\n")
   print(f"Midterm Grade: {self.__midterm}\n")
   print(f"Final Grade: {self.__finals}\n")
   print(f"Average: {round(self.grades(),2)}\n")

class Student_1(Person):
  pass

class Student_2(Person):
  pass

class Student_3(Person):
  pass

student1 = Student_1("student 1", 90, 91, 95)
student1.display()

student2 = Student_2("student 2", 80, 87, 96)
student2.display()

student3 = Student_3("student 3", 87, 90, 92)
student3.display()