# [ LeetCode ] 362. Design Hit Counter

def solution(input: list[tuple[str, int]]) -> list[int]:
    class HitCounter:
        
        def __init__(self):
            self.duration: int = 300
            self.timestamps: dict[int, int] = {}

        def hit(self, timestamp: int) -> None:
            for time in range(timestamp, timestamp+self.duration):
                if time in self.timestamps:
                    self.timestamps[time] += 1
                else:
                    self.timestamps[time] = 1

        def getHits(self, timestamp: int) -> int:
            if timestamp in self.timestamps:
                return self.timestamps[timestamp]
            else:
                return 0
    
    answer: list[int | None] = []
    for operation, value in input:
        if operation == "HitCounter":
            hit_count = HitCounter()
            answer.append(None)
        
        elif operation == "hit":
            hit_count.hit(timestamp=value)
            answer.append(None)
        
        else:
            count: int = hit_count.getHits(timestamp=value)
            answer.append(count)
    
    return answer


def another_solution(input: list[tuple[str, int]]) -> list[int]:
    class HitCounter:
        
        def __init__(self):
            self.duration: int = 300
            self.bucket: list[tuple[int, int]] = [
                (time, 0) for time in range(self.duration)
            ]

        def hit(self, timestamp: int) -> None:
            index: int = (timestamp - 1) % self.duration
            time, count = self.bucket[index]
            if time == timestamp:
                self.bucket[index] = (time, count+1)
            else:
                self.bucket[index] = (timestamp, 1)

        def getHits(self, timestamp: int) -> int:
            answer: int = 0
            for time, count in self.bucket:
                if (timestamp - time) < 300:
                    answer += count
                
            return answer
    
    
    answer: list[int | None] = []
    for operation, value in input:
        if operation == "HitCounter":
            hit_count = HitCounter()
            answer.append(None)
        
        elif operation == "hit":
            hit_count.hit(timestamp=value)
            answer.append(None)
        
        else:
            count: int = hit_count.getHits(timestamp=value)
            answer.append(count)
    
    return answer


def binary_search_solution(input: list[tuple[str, int]]) -> list[int]:
    class HitCounter:
        
        def __init__(self):
            self.bucket: list[int] = []

        def hit(self, timestamp: int) -> None:
            self.bucket.append(timestamp)

        def getHits(self, timestamp: int) -> int:
            left, right = 0, len(self.bucket) - 1
            target: int = timestamp - 300
            while left <= right:
                middle = (left + right) // 2
                if self.bucket[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            
            return len(self.bucket) - left
    
    
    answer: list[int | None] = []
    for operation, value in input:
        if operation == "HitCounter":
            hit_count = HitCounter()
            answer.append(None)
        
        elif operation == "hit":
            hit_count.hit(timestamp=value)
            answer.append(None)
        
        else:
            count: int = hit_count.getHits(timestamp=value)
            answer.append(count)
    
    return answer


if __name__ == "__main__":
    case: dict[str, list[str] | list[int]] = {
        "input": {
            "operations": [
                "HitCounter", "hit", "hit", "hit",
                "getHits", "hit", "getHits", "getHits"
            ],
            "values": [
                [None], [1], [2], [3], [4], [300], [300], [301]                
            ],
        },
        "output": [None, None, None, None, 3, None, 4, 3]
    }
    input: list[tuple[str, int]] = []
    for operation, value in zip(
        case["input"]["operations"], case["input"]["values"]
    ):
        input.append((operation, value[0]))
    
    assert case["output"] == solution(input=input)
    assert case["output"] == another_solution(input=input)
    assert case["output"] == binary_search_solution(input=input)
    