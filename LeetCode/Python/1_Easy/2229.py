# [ LeetCode ] 2229. Check if an Array Is Consecutive

def solution(nums: list[int]) -> bool:
    minimum_number, length = 10 ** 5 + 1, len(nums)
    numbers: dict[int, bool] = {}
    for number in nums:
        if number < minimum_number:
            minimum_number = number
        
        if number in numbers:
            return False
        else:
            numbers[number] = True
    
    for number in range(minimum_number, minimum_number+length):
        if number in numbers:
            numbers.pop(number)
        else:
            return False

    return True if not numbers else False


def another_solution(nums: list[int]) -> bool:
    x, n, unique_nums = min(nums), len(nums), set(nums)
    if len(unique_nums) == n:
        for number in nums:
            if number < x or number > (x + n - 1):
                return False
        return True
        
    else:
        return False
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | bool]] = [
        {
            "input": { "nums": [1, 3, 4, 2] },
            "output": True
        },
        {
            "input": {
                "nums": [3, 5, 4]
            },
            "output": True
        },
        {
            "input": {
                "nums": [3, 3, 5, 4]
            },
            "output": False
        },        
        {
            "input": {
                "nums": [1, 3]
            },
            "output": False
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        