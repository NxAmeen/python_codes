class Teacher:

    school_name='ABC'

    def __init__(self,subject):
        self.subject=subject
        self.subject=input("Enter the subject:")

    def print_details(self):
        print(self.subject)




class Student(Teacher):

    def student_details(self,name,age):
        self.name=name
        self.age=age
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))

    def print_student_details(self):
        print(self.name,self.age)




class Parent(Student):

    def print_parent(self):
        print("This is a parent class")



print(Teacher.school_name)

s1=Parent('')
s1.student_details('','')
s1.print_student_details()
s1.print_details()