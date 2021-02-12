def twoSum(nums: list[int], target: int) -> list[int]:
    temp = {}
    for idx, num in enumerate(nums):
        if (target - num) in temp:
            return [temp[target - num], idx]
        else:
            temp[num] = idx


if __name__ == "__main__":
    nums   = [2, 7, 11, 15]
    target = 9

    print(twoSum(nums, target))
    