from functools import reduce
def reduce(a,b):
    return a+b
elements=[1,2,3,4,5]
sum_of_num=reduce(reduce,elements)
print(sum_of_num)