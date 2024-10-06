import re
def Is_Valid(numbers):
    pattern='^[6-9]\d{9}$'
    math_number=re.match(pattern,numbers)
    return math_number

phone_number=input("Enter a phone number:")
result = Is_Valid(phone_number)

if result:
    print(f"{phone_number} valid phone number")
else:
    print(f"{phone_number} invalid phone number")