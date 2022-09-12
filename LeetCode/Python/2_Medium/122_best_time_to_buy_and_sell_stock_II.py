# [ LeetCode ] 122. Best Time to Buy and Sell Stock II

def solution(prices: list[int]) -> int:
    answer: int = 0
    current_min: int = prices[0]
    for idx in range(1, len(prices)-1):
        if prices[idx] < current_min:
            current_min = prices[idx]
        elif prices[idx] > prices[idx+1]:
                answer += (prices[idx] - current_min)
                current_min = prices[idx]
    
    if prices[len(prices)-1] > current_min:
        answer += (prices[len(prices)-1] - current_min)
    
    return answer


def another_solution(prices: list[int]) -> int:
    answer: int = 0
    for idx in range(1, len(prices)):
        if prices[idx] > prices[idx-1]:
            answer += (prices[idx] - prices[idx-1])
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": { "prices": [7, 1, 5, 3, 6, 4] },
            "output": 7
        },
        {
            "input": { "prices": [1, 2, 3, 4, 5] },
            "output": 4
        },
        {
            "input": { "prices": [7, 6, 4, 3, 1] },
            "output": 0
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        