def simple_interest(p,t,r):
    print("The value of p is: ",p)
    print("The value of t is: ",t)
    print("The value of r is: ",r)

    si = (p*t*r)/100
    return si

a = int (input("The value of a is: "))
b = int (input("The value of b is: "))
c = int (input("The value of c is: "))
print(simple_interest(a,b,c))

