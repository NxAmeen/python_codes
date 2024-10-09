# x=10
# y=20
# # print(x+y)
# def myFun():
#     print(x+y)
# myFun()
# str1="Hello"
# str2="World"
# print(str1[::-1])
# print(str2*3)
# print(str1.islower())




# a=10
# b='My age is {}'
# print(b.format(a))
# str3=" Hello World "
# print(str3.strip())
# print(str3.replace("World","Guys"))
# print(str3.split())



# str4=str3.split(',')
# print(str4)



# a=['banana','apple',10,True]
# c=list('banana')
# a[1:0]=['mango','orange']



# a.append('grapes')
# b=['kiwi','grapes']
# a.insert(1,'kiwi')
# a.extend(b)



# b.remove('kiwi')
# a.pop(1)



# print(a,c)
# print(a[1:3]) 



# set_data={'apple','banana','mango',"apple","apple"}
# set_data2=('apple','banana','mango',"apple","apple")
# set_data.add('orange')
# set_data.update(set_data2)
# print(set_data)



# dict1={'name':'John','age':25,'city':'New York'}
# dict2=dict(name='Abraham',age=35,city='USA')
# print(dict,dict2)




# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end='')
#         j+=1
#     print()
#     i+=1



# n=5
# i=1
# while i<=n:
#     j=1
#     while j<i:
#         print(' ',end=" ")
#         j+=1



#     while j<=n:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1



# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
    


# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
    


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(chr(j+65),end=" ")
#     print()



# for i in range(1,10):
#     if i%2==0:
#         continue
#     print(i)



# lang=['Python','Java','C++','C#']
# new_lst=[i for i in lang if 'P' in i]
# print(new_lst)



# def myFun(a,b):
#      print(a*b)
# myFun(1,20)



# def Fun(*sum):
#     total=0
#     for num in sum:
#         total+=num
#     return total
# print(Fun(10,20,30,40))



# def fun(**kwargs):
#     print(kwargs,type(kwargs))
# fun(name='John',age=25,city='New York')



# def square(num):
#     return num*num
# x=int(input("Enter a number:"))
# print(square(x))



class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        self.name=input("Enter your name:")
        self.age=input("Enter your age:")
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

p1=Person()
p1.details("","")
p1.display()