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

    