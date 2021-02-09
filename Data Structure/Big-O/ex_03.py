def ex_03(array: list):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            print(array[i], array[j])