# [ LeetCode ] 1056. Confusing Number

def solution(n: int) -> bool:
    rotated_number: dict[str, str] = {
        "0": "0", "1": "1", "6": "9", "8": "8", "9": "6"
    }
    converted_number: str = str(n)
    for number in converted_number:
        if number not in rotated_number:
            return False
    left, right = 0, len(converted_number) - 1
    while left <= right:
        left_number: str = converted_number[left]
        right_number: str = converted_number[right]
        if (
            left_number != rotated_number[right_number]
            or
            right_number != rotated_number[left_number]
        ):
            return True
        left += 1
        right -= 1
    return False


def another_solution(n: int) -> bool:
    rotated_number: dict[int, int] = { 0: 0, 1: 1, 6: 9, 8: 8, 9: 6 }
    copied_n: int = n
    rotated_result: int = 0
    while copied_n:
        remainder: int = copied_n % 10
        if remainder not in rotated_number:
            return False
        rotated_result = rotated_result * 10 + rotated_number[remainder]
        copied_n //= 10
    return rotated_result != n
