# [ LeetCode ] 1346. Check If N and Its Double Exist

def solution(arr: list[int]) -> bool:
    bucket: dict[int, int] = { number: 0 for number in range(-2000, 2001) }
    for number in arr:
        bucket[number] += 1
    
    for number, count in bucket.items():
        if number == 0 and count >= 2:
            return True
        elif number != 0 and count > 0 and bucket[number * 2] > 0:
            return True
    
    return False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | bool]] = [
        {
            "input": {
                "arr": [10, 2, 5, 3]
            },
            "output": True
        },
        {
            "input": {
                "arr": [3, 1, 7, 1]
            },
            "output": False
        },
        {
            "input": {
                "arr": [-4, 0]
            },
            "output": False
        },
        {
            "input": {
                "arr": [0, 0]
            },
            "output": True
        },
        {
            "input": {
                "arr": [-900, 0, 700]
            },
            "output": False
        }                                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        