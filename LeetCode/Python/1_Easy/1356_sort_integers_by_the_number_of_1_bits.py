# [ LeetCode ] 1356. Sort Integers by The Number of 1 Bits

def solution(arr: list[int]) -> list[int]:
    numbers: dict[int, list[int]] = {}
    for number in arr:
        count: int = 0
        for binary in str(bin(number)):
            if binary == "1":
                count += 1
        
        if count in numbers:
            numbers[count].append(number)
        
        else:
            numbers[count] = [number]
    
    answer: list[int] = []
    for count, same_count_numbers in sorted(numbers.items(), key=lambda x: x[0]):
        same_count_numbers.sort()
        answer.extend(same_count_numbers)
    
    return answer


def another_solution(arr: list[int]) -> list[int]:
    return sorted(arr, key=lambda number: (bin(number).count("1"), number))


def bit_manipulation(arr: list[int]) -> list[int]:
    def hamming_weight(number: int) -> int:
        weight: int = 0
        while number:
            weight += 1
            number &= (number - 1)
        
        return weight
    
    
    return sorted(
        arr, key=lambda number: (hamming_weight(number=number), number)
    )


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | list[int]]] = [
        {
            "input": { "arr": [0, 1, 2, 3, 4, 5, 6, 7, 8] },
            "output": [0, 1, 2, 4, 8, 3, 5, 6, 7]
        },
        {
            "input": { "arr": [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1] },
            "output": [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        }        
    ]
    for case in cases:
        assert case["output"] == solution(arr=case["input"]["arr"])
        assert case["output"] == another_solution(arr=case["input"]["arr"])
        assert case["output"] == bit_manipulation(arr=case["input"]["arr"])
    