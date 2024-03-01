def compound_interest(p,r,t):
    Amount = p*(pow((1+r/100),t))
    CI = Amount - p
    print(CI)


p = int(input("Enter the value of p: "))
r = float(input("Enter the value of r: "))
t = int(input("Enter the value of t: "))
compound_interest(p,r,t)