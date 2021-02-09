def ex_11(n: int):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * ex_11(n - 1)