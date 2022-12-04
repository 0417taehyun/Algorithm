# [ LeetCode ] 2256. Minimum Average Difference

def solution(nums: list[int]) -> int:
    def create_prefix_sum(nums: list[int], is_right_to_left: bool) -> list[int]:
        prefix_sum: list[int] = []
        if is_right_to_left:
            prefix_sum.append(0)
        accumulate_sum: int = 0
        index: int = 0
        while len(prefix_sum) < len(nums):
            accumulate_sum += nums[index]
            sum_average: int = accumulate_sum // (index + 1)
            prefix_sum.append(sum_average)
            index += 1
        return prefix_sum
    
    
    answer: int = 0
    minimum_average_difference: int = 10 ** 5
    left_to_right_prefix_sum: list[int] = create_prefix_sum(nums, False)
    right_to_left_prefix_sum: list[int] = create_prefix_sum(nums[::-1], True)
    for idx, (left_sum, right_sum) in enumerate(
        zip(left_to_right_prefix_sum, right_to_left_prefix_sum[::-1])
    ):
        target: int = abs(left_sum - right_sum)
        if target < minimum_average_difference:
            answer = idx
            minimum_average_difference = target

    return answer


if __name__ == "__main__":
    cases: dict[str, dict[str, list[int]] | int] = [
        {
            "input": { "nums": [ 2, 5, 3, 9, 5, 3 ] },
            "output": 3
        },
        {
            "input": { "nums": [ 0 ] },
            "output": 0
        },
        {
            "input": { "nums": [ 4, 2, 0 ] },
            "output": 2
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        