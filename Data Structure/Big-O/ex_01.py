def ex_01(array: list):
    sum  = 0
    prod = 1

    for idx in range(len(array)):
        sum += array[idx]

    for idx in range(len(array)):
        prod += array[idx]

    print(sum, prod)