def ex_05(first_array: list, second_array: list):
    for i in range(len(first_array)):
        for j in range(len(second_array)):
            for k in range(100000):
                print(first_array[i], second_array[j])