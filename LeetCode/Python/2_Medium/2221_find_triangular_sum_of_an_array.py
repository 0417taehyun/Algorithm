# [ LeetCode ] 2221. Find Triangular Sum of an Array

def solution(nums: list[int]) -> int:
    answer: int = 0
    while nums:
        for index in range(len(nums) - 1):
            nums[index] = (nums[index] + nums[index + 1]) % 10
        
        answer = nums.pop()
        
    return answer


def another_solution(nums: list[int]) -> int:
    def combinator(n: int, r: int) -> int:
        top, bottom = 1, 1
        for number in range(n, n - r, -1):
            top *= number
        for bottom in range(r, 0, -1):
            bottom *= bottom
        
        return top // bottom

    answer: int = 0
    n: int = len(nums) - 1
    for index, number in enumerate(nums):
        answer += (combinator(n=n, r=index) * number)
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": { "nums": [1,2,3,4,5] },
            "output": 8
        },
        {
            "input": { "nums": [5] },
            "output": 5
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        