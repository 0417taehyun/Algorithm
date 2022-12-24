# [ LeetCode ] 393. UTF-8 Validation

def solution(data: list[int]) -> bool:
    from collections import deque
    
    
    def get_followed_counts() -> int:
        target: int = queue.popleft()
        if target >= min_four and target < max_four:
            if len(queue) < 3:
                return -1
            else:
                return 3
        elif target >= min_three and target < max_three:
            if len(queue) < 2:
                return -1
            else:
                return 2
        elif target >= min_two and target < max_two:
            if len(queue) < 1:
                return -1
            else:
                return 1
        elif target >= min_one and target < max_one:
            return 0
        else:
            return -1
        
    
    def validate_followed_bytes(count: int) -> bool:
        while count:
            target: int = queue.popleft()
            if target >= min_followed and target < max_followed:
                count -= 1
            else:
                return False

        return True
    
    
    queue: deque = deque(data)
    max_four, min_four = int("11111000", 2), int("11110000", 2)
    max_three, min_three = int("11110000", 2), int("11100000", 2)
    max_two, min_two = int("11100000", 2), int("11000000", 2)
    max_one, min_one = int("10000000", 2), int("0000000", 2)
    max_followed, min_followed = int("11000000", 2), int("10000000", 2)
    
    while queue:
        count: int = get_followed_counts()
        if count >= 0:
            if not validate_followed_bytes(count=count):
                return False
        else:
            return False
    
    return True


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | bool]] = [
        {
            "input": { "data": [197, 130, 1] },
            "output": True
        },
                {
            "input": { "data": [235, 140, 4] },
            "output": False
        },
        {
            "input": { "data": [255] },
            "output": False
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        