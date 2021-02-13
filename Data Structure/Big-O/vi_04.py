def vi_04(first_num: int, second_num: int):
    count = 0
    num_sum = second_num

    while num_sum <= first_num:
        num_sum += second_num
        count += 1

    return count