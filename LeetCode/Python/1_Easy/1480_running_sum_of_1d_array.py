# [ LeetCode ] 1480. Running Sum of 1d Array

def solution(nums: list[int]) -> list[int]:
    answer: list[int] = [ nums[0] ]
    for i in range(1, len(nums)):
        accumulate: int = answer[i-1] + nums[i]
        answer.append(accumulate)
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | list[int]]] = [
        {
            "input": { "nums": [1, 2, 3, 4] },
            "output": [1, 3, 6, 10]
        },
        {
            "input": { "nums": [1, 1, 1, 1, 1] },
            "output": [1, 2, 3, 4, 5]
        },
        {
            "input": { "nums": [3, 1, 2, 10, 1] },
            "output": [3, 4, 6, 16, 17]
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
