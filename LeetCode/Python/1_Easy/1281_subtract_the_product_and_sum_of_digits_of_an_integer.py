# [ LeetCode ] 1281. Subtract the Product and Sum of Digits of an Integer

def solution(n: int) -> int:
    product_of_digits: int = 1
    sum_of_digits: int = 0
    for number in str(n):
        product_of_digits *= int(number)
        sum_of_digits += int(number)
    return product_of_digits - sum_of_digits


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | int]] = [
        {
            "input": {"n": 234},
            "output": 15
        },
        {
            "input": {"n": 4421},
            "output": 21
        }        
    ]
    for case in cases:
        assert case["output"] == solution(n=case["input"]["n"])
    