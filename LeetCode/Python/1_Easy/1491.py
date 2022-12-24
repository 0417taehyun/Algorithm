# [ LeetCode ] 1491. Average Salary Excluding the Minimum and Maximum Salary

def solution(salary: list[int]) -> float:
    return (sum(salary) - max(salary) - min(salary)) // (len(salary) - 2)


if __name__ == "__main__":
    cases: list[dict[str, list[int] | float]] = [
        {
            "input": [4000, 3000, 1000, 2000],
            "output": 2500.00000
        },
        {
            "input": [1000, 2000, 3000],
            "output": 2000.00000        
        }
    ]
    for case in cases:
        assert case["output"] == solution(salary=case["input"])
    