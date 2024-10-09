def even(num):
    if num%2==0:
        return True

elements=[1,2,3,4,5]
print(list(filter(even,elements)))