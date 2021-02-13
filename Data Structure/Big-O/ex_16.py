def ex_16(n: int):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        prev = ex_16(n / 2)
        curr = prev * 2
        return curr