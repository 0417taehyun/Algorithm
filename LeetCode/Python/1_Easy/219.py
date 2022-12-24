# [ LeetCode ] 219. Contains Duplicate II


def soltuion(nums: list[int], k: int) -> bool:
    number_with_index: dict[int, int] = {}
    for idx, number in enumerate(nums):
        if number in number_with_index:
            if idx - number_with_index[number] <= k:
                return True
            
            else:
                number_with_index[number] = idx
                
        else:
            number_with_index[number] = idx

    return False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int] | bool]] = [
        {
            "input": {
                "nums": [1, 2, 3, 1],
                "k": 3
            },
            "output": True
        },
        {
            "input": {
                "nums": [1, 0, 1, 1],
                "k": 1
            },
            "output": True
        },
        {
            "input": {
                "nums": [1, 2, 3, 1, 2, 3],
                "k": 2
            },
            "output": False
        }
    ]
    for case in cases:
        assert case["output"] == soltuion(
            nums=case["input"]["nums"], k=case["input"]["k"]
        )
        