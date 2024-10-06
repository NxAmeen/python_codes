a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
try:
    even_numbers = [2, 4, 6, 8, 10]
    print(even_numbers[2])
    print(a/b)

except IndexError:
    print("Index out of range")

except NameError:
    print("Name not defined")

except ZeroDivisionError:
    print("Division by zero not possible")




def avg(marks):
    try:
        assert len(marks) != 0
        return sum(marks)/len(marks)
    except AssertionError as msg:
        print(msg)

marks = [10, 20, 30, 40, 50]
print("Average of marks:",avg(marks))

marks1 = []
print("Average of marks:",avg(marks1))