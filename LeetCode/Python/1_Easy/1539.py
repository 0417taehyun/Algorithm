# [ LeetCode ] 1539. Kth Missing Positive Number

def solution(arr: list[int], k: int) -> int:
    bucket: list[int] = [0] * 2001
    for number in arr:
        bucket[number] += 1
    
    for number in range(1, 2001):
        if bucket[number] == 0:
            k -= 1
            if k == 0:
                return number


def another_soluiton(arr: list[int], k: int) -> int:
    start, end = 0, len(arr) - 1
    while start <= end:
        middle: int = start + (end - start) // 2
        if arr[middle] - middle - 1 < k:
            start = middle + 1
        else:
            end = middle - 1
    
    return k + start


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int] | int]] = [
        {
            "input": {
                "arr": [2, 3, 4, 7, 11],
                "k": 5
            },
            "output": 9
        },
        {
            "input": {
                "arr": [1, 2, 3, 4],
                "k": 2
            },
            "output": 6
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        