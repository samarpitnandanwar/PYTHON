import math

def isArmstrong(num):
    n = num
    numDigits = 0
    sum = 0

    while n > 0:
        n //= 10
        numDigits += 1
    
    n = num

    while n > 0:
        digit = n % 10
        sum += math.pow(digit, numDigits)
        n //= 10


    if sum == num:
        return True
    return False

a = 1535
if isArmstrong(a):
    print(a, "is armstrong")
else:
    print(a, "is not armstrong")