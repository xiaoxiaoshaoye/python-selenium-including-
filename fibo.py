# coding=utf-8
def fib(n):
    a,b = 0,1
    while b < n:
        a,b = b,a+b
        print(a,b)


def fib2(n):
    result=[]
    a,b = 0,1
    while b < n:
        a,b = b,a+b
        result.append(b)
        return  result