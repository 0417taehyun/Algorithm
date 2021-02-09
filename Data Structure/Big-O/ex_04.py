def ex_04(first_array: list, second_array: list):
    for i in range(len(first_array)):
        for j in range(len(second_array)):
            if first_array[i] < second_array[j]:
                print(first_array[i], second_array[j])
