# [ LeetCode ] 1523. Count Odd Numbers in an Interval Range

def solution(low: int, high: int) -> int:
    answer: int = (high - low) // 2
    if (high % 2) or (low % 2):
        answer += 1
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[dict[str, int] | int]]] = [
        {
            "input": {"low": 3, "high": 7},
            "output": 3
        },
        {
            "input": {"low": 8, "high": 10},
            "output": 1
        }        
    ]
    