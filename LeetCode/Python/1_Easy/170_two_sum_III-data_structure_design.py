# [ LeetCode ] 170. Two Sum III - Data structure design

def solution(operators: list[tuple[str, int]]) -> list[bool | None]:
    class TwoSum:
        def __init__(self) -> None:
            self.numbers: list[int] = []
            
        def add(self, number: int) -> None:
            self.numbers.append(number)
            
        def find(self, value: int) -> bool:
            self.numbers.sort()
            left, right = 0, len(self.numbers) - 1
            while left < right:
                target: int = self.numbers[left] + self.numbers[right]
                if target == value:
                    return True
                elif target > value:
                    right -= 1
                else:
                    left += 1
            
            return False
        
        
    answer: list[bool | None] = []
    for operator, number in operators:
        if operator == "TwoSum":
            cls: TwoSum = TwoSum()
            answer.append(None)
        
        elif operator == "add":
            result = cls.add(number)
            answer.append(result)
        
        else:
            result = cls.find(number)
            answer.append(result)
    
    return answer
    

def another_solution(operators: list[tuple[str, int]]) -> list[bool | None]:
    class TwoSum:
        def __init__(self) -> None:
            self.numbers: dict[int, int] = {}
        
        def add(self, number: int) -> None:
            if number in self.numbers:
                self.numbers[number] += 1
            else:
                self.numbers[number] = 1
        
        def find(self, value: int) -> bool:
            for number in self.numbers.keys():
                target: int = value - number
                if (
                    target in self.numbers
                    and
                    (target != number or self.numbers[target] > 1)
                ):
                    return True
                    
            return False
    
    
    answer: list[bool | None] = []
    for operator, number in operators:
        if operator == "TwoSum":
            cls: TwoSum = TwoSum()
            answer.append(None)
        
        elif operator == "add":
            result = cls.add(number)
            answer.append(result)
        
        else:
            result = cls.find(number)
            answer.append(result)
    
    return answer


if __name__ == "__main__":
    cases: list[
        dict[str, dict[str, list[tuple[str, int]]] | list[bool | None]]
    ] = [
            {
                "input": {
                    "operators": [
                        ("TwoSum", None), ("add", 1), ("add", 3), ("add", 5),
                        ("find", 4), ("find", 7)
                    ]
                },
                "output": [None, None, None, None, True, False]
            },
            {
                "input": {
                    "operators": [
                        ("TwoSum", None), ("add", 0), ("find", 0)
                    ]
                },
                "output": [None, None, False]
            },
            {
                "input": {
                    "operators": [
                        ("TwoSum", None), ("add", 0), ("add", 0), ("find", 0)
                    ]
                },
                "output": [None, None, None, True]
            },                    
    ]
    for case in cases:
        assert case["output"] == solution(
            operators=case["input"]["operators"]
        )
        assert case["output"] == another_solution(
            operators=case["input"]["operators"]
        )