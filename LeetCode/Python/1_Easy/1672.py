# [ LeetCode ] 1672. Richest Customer Wealth

def solution(accounts: list[list[int]]) -> int:
    answer: int = 0
    for customer in accounts:
        total: int = sum(customer)
        answer = max(answer, total)
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[list[int]]] | int]] = [
        {
            "input": { "accounts": [[1, 2, 3], [3, 2, 1]] },
            "output": 6
        },
        {
            "input": { "accounts": [[1, 5], [7, 3], [3, 5]] },
            "output": 10
        },
        {
            "input": { "accounts": [[2, 8, 7], [7, 1, 3], [1, 9, 5]] },
            "output": 17
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
