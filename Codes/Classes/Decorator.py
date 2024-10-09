def minus_decor(fun):
    def wrapper(x,y):
        if x<y:
            x,y=y,x
        return fun(x,y)
    return wrapper

@minus_decor
def minus(x,y):
    print(x-y)


minus(5,10)