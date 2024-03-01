n = 153
s = n
b = len(str(n))
sum1 = 0
while n!=0:
    r = n%10
    sum2 = sum1 + (r**b)
    n = n//10
if s == sum1:
    print("The given numner", s,"is armstrong number")
else:
    print("The given number", s,"is armstrong number")