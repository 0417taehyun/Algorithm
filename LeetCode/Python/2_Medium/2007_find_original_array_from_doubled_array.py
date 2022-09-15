# [ LeetCode ] 2007. Find Original Array From Doubled Array

def solution(changed: list[int]) -> list[int]:
    if len(changed) % 2 == 0:    
        answer: list[int] = []
        numbers: dict[int, int] = {}
        for number in sorted(changed):
            if number in numbers:
                if numbers[number] == 1:
                    numbers.pop(number)
                else:
                    numbers[number] -= 1
                answer.append(number//2)
            else:
                if number * 2 in numbers:
                    numbers[number*2] += 1
                else:
                    numbers[number*2] = 1

        return answer if not numbers else []
        
    else:
        return []
    

def another_solution(changed: list[int]) -> list[int]:
    if len(changed) % 2 == 0:
        answer: list[int] = []
        bucket: list[int] = [ 0 for _ in range(max(changed)*2+1) ]
        for number in changed:
            bucket[number] += 1
        number: int = 0
        while number < len(bucket):
            if bucket[number] > 0:
                if bucket[number*2] > 0:
                    answer.append(number)
                    bucket[number] -= 1
                    bucket[number*2] -= 1
                else:
                    return []
            else:
                number += 1
          
        return answer
    
    else:
        return []


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | list[int]]] = [
        {
            "input": { "changed": [1, 3, 4, 2, 6, 8] },
            "output": [1, 3, 4]
        },
        {
            "input": { "changed": [6, 3, 0, 1] },
            "output": []
        },
        {
            "input": { "changed": [1] },
            "output": []
        },
        {
            "input": { "changed": [2, 1] },
            "output": [1]
        },
        {
            "input": { "changed": [0, 0, 0, 0] },
            "output": [0, 0]
        }                         
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        