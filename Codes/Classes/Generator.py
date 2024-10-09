def generate_square(lst):
    for item in lst:
        yield item**2
numbers=[1,2,3,4,5]
my_gen=generate_square(numbers)
for i in my_gen:
    print(i)