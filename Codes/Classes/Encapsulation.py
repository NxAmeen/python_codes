class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


class manager(employee):
    def print_details(self,company):
        self.company=company
        print(self.name, self.salary, self.company)


obj = manager('John', 10000)
obj.display()
obj.print_details('Google')