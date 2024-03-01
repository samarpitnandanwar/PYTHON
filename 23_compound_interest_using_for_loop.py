def compound_interest(p,r,t):
    Amount = p
    for i in range(t):
        Amount = Amount*(1+r/100)

    CI = Amount - p
    print(CI)

compound_interest(1200,5.4,2)