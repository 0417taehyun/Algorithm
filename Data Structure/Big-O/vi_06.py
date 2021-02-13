def vi_06(n: int):
    guess = 1
    while (guess * guess) <= n:
        if (guess * guess) == n:
            return guess

        guess += 1

    return -1