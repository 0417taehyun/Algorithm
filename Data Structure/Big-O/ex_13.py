def ex_13(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ex_13(n - 1) + ex_13(n + 1)