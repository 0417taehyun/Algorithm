# [ LeetCode ] 121. Best Time to Buy and Sell Stock

def solution(prices: list[int]) -> int:
    buy: int = prices[0]
    answer: int = 0
    for idx in range(1, len(prices)):
        if prices[idx] < buy:
            buy = prices[idx]
        elif (prices[idx] - buy) > answer:
            answer = prices[idx] - buy
    return answer


if __name__ == "__main__":
    cases: list[str, dict[str, list[int]] | int] = [
        {
            "input": { "prices": [7, 1, 5, 3, 6, 4] },
            "output": 5
        },
        {
            "input": { "prices": [7, 6, 4, 3, 1] },
            "output": 0
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        