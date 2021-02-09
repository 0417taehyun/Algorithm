def ex_06(array: list):
    for idx in range(len(array) / 2):
        other = len(array) - idx - 1
        temp  = array[idx]

        array[idx], array[other] = array[other], temp