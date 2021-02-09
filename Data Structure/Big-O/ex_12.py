def permutation(string: str):
    return permutation(string, "")


def ex_12(string: str, prefix: str):
    if len(string) == 0:
        print(prefix)
    else:
        for idx in range(len(string)):
            rem = string[:idx] + string[idx + 1:]
            permutation(rem, prefix + string[idx])