# [ LeetCode ] 1342. Number of Steps to Reduce a Number to Zero

def solution(num: int) -> int:
    answer: int = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        answer += 1
    return answer


def bitwise_solution(num: int) -> int:
    answer: int = 0
    while num > 0:
        if (num & 1) == 0:
            num >>= 1
        else:
            num -= 1
        answer += 1
    return answer


def bitcount_solution(num: int) -> int:
    answer: int = 0
    bits: str = bin(num)[2:]
    for bit in bits:
        if bit == "0":
            answer += 1
        else:
            answer += 2
    return answer - 1


def bitcount_with_bitmask_solution(num: int) -> int:
    answer: int = 0
    if num == 0:
        return answer
    
    bitmask: int = 1
    while bitmask <= num:
        if (num & bitmask) == 0:
            answer += 1
        else:
            answer += 2
        bitmask *= 2
    return answer - 1
