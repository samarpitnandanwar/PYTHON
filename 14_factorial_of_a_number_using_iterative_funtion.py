def factorial(n):

    # example 1
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        while(n>1):
            fact*=n
            n-=1
        return fact

    # example 2
    # res = 1
    # for i in range(2, n+1):
    #     res *= i
    # return res
    
   
a = 5
print(factorial(a))