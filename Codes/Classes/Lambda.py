def lam(n):
    return lambda x:x * n
    
result=lam(5)
print('Double the number:',result(2))