# [ 프로그래머스 ] 입국심사

def solution(n: int, times: list[int]) -> int:
    times.sort()
    start, end = times[0], times[-1] * n
    
    while start <= end:
        count: int = 0
        middle: int = (start + end) // 2
        
        for time in times:
            count += (middle // time)
        
        if count < n:
            start = middle + 1
        
        else:
            answer: int = middle
            end = middle - 1
    
    return answer


if __name__ == "__main__":
    case: dict[str, dict[str, int | list[int]] | int] = {
        "input": {"n": 6, "times": [7, 10]}, "output": 28
    }
    assert case["output"] == solution(n=case["input"]["n"], times=case["input"]["times"])
    