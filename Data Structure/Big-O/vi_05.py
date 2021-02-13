def sqrt_helper(n: int, min_n: int, max_n: int):
    if max_n < min_n:
        return -1
    guess = (min_n + max_n) / 2

    if (guess * guess) == n:
        return guess
    elif (guess * guess) < n:
        return sqrt_helper(n ,guess + 1, max_n)
    else:
        return sqrt_helper(n, min_n, guess - 1)


def vi_05(n: int):
    return sqrt_helper(n, 1, n)