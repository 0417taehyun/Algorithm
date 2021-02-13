def fib(n: int, memo: list):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def ex_15(n: int):
    memo = [ 0 for i in range(n + 1) ]
    for i in range(n):
        print(fib(i, memo))