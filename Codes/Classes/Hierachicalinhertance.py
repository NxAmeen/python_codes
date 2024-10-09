class Details:
    def __init__(self,id,name,address):
        self.id=id
        self.name=name
        self.address=address

    def set_details(self):
        self.id=int(input("Enter the id:"))
        self.name=input("Enter the name:")
        self.address=input("Enter the address:")

    def print_details(self):
        print('ID: \n Name: \n Address: ',self.id,self.name,self.address)

class Employee(Details):
    def get_imp_details(self,company):
        self.company=company
        self.company=input("Enter the company name:")

    def print_emp_details(self):
        print('Company:',self.company)

class Manager(Details):
    def get_salary_details(self,salary):
        self.salary=salary
        self.salary=int(input("Enter the salary:"))

    def print_salary_details(self):
        print('Salary:',self.salary)


print('Employee Details')
e1=Employee("","","")
e1.set_details()
e1.get_imp_details("") 
e1.print_details()
e1.print_emp_details()

print('Manager Details')
m1=Manager("","","")
m1.set_details()
m1.get_salary_details("")
m1.print_details()
m1.print_salary_details()