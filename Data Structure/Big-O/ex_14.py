def fib(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def ex_14(n: int):
    for i in range(len(n)):
        print(fib(i))