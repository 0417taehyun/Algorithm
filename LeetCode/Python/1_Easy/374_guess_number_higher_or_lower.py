# [ LeetCode ] 374. Guess Number Higher or Lower

def guess(num: int) -> int:
    """
    pre-defined API
    """
    pass


def solution(n: int) -> int:
    start, end = 1, n
    while start <= end:
        middle: int = (start + end) // 2
        result: int = guess(num=middle)
        if result == 0:
            return middle
        elif result == 1:
            start = middle + 1
        else:
            end = middle - 1
    