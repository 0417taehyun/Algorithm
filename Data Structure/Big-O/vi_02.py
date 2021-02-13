def vi_02(first_num: int, second_num: int):
    if second_num < 0:
        return 0
    elif second_num == 0:
        return 1
    else:
        return first_num * vi_02(first_num, second_num - 1)