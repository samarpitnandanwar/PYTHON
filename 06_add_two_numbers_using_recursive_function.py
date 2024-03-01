def recursive(x,y):
    if y == 0:
        return x
    else:
        return recursive(x+1, y-1)
    

a = 2
b = 4
sum = recursive(a,b)
print(sum)