from math import sqrt


def ex_10(n: int):
    x = 2
    
    while x * x <= n:
        if n % x == 0:
            return False

        x += 1
        
    return True


def ex_10_2(n: int):
    for x in range(2, sqrt(n) + 1):
        if n % x == 0:
            return False

    return True