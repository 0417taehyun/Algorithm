def vi_03(first_num: int, second_num: int):
    if second_num <= 0:
        return -1
    div = first_num / second_num
    return first_num - (div * second_num)