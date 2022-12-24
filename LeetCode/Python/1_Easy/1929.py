# [ LeetCode ] 1929. Concatenation of Array

def solution(nums: list[int]) -> list[int]:
    return nums + nums


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | list[int]]] = [
        {
            "input": {"nums": [1, 2, 1]},
            "output": [1, 2, 1, 1, 2, 1]
        },
        {
            "input": {"nums": [1, 3, 2, 1]},
            "output": [1, 3, 2, 1, 1, 3, 2, 1]
        }        
    ]
    for case in cases:
        assert case["output"] == solution(nums=case["input"]["nums"])
    