# [ 백준 ] 4673번: 셀프 넘버

def solution() -> None:
    nums: dict[int, int] = { num + 1: 0 for num in range(10000) }
    for num in range(10000):
        constructed_num: int = (num + 1) + sum([ int(n) for n in str(num + 1) ])
        if constructed_num <= 10000:
            nums[constructed_num] += 1
    
    for num, count in nums.items():
        if not count:
            print(num)
        

if __name__ == "__main__":
    solution()
    