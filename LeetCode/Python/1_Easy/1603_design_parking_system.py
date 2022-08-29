# [ LeetCode ] 1603. Design Parking System

class Solution:
    def __init__(self, big: int, medium: int, small: int):
        self.big_slots: int = big
        self.medium_slots: int = medium
        self.small_slots: int = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_slots > 0:
                self.big_slots -= 1
                return True
            else:
                return False
        
        elif carType == 2:
            if self.medium_slots > 0:
                self.medium_slots -= 1
                return True
            else:
                return False
        
        else:
            if self.small_slots > 0:
                self.small_slots -= 1
                return True
            else:
                return False


class AnotherSolution:
    def __init__(self, big: int, medium: int, small: int) -> None:
        self.slots: list[int] = [big, medium, small]
    
    def addCar(self, carType: int) -> bool:
        if self.slots[carType - 1] > 0:
            self.slots[carType - 1] -= 1
            return True
        
        else:
            return False


if __name__ == "__main__":
    case: dict[str, dict[str, list[str] | list[list[int]] | list[bool]]] = {
        "input": {
            "operations": [
                "ParkingSystem", "addCar", "addCar", "addCar", "addCar"
            ],
            "data": [[1, 1, 0], [1], [2], [3], [1]]
        },
        "output": [None, True, True, False, False]
    }
    solution_answer: list[bool] = [None]
    another_solution_answer: list[bool] = [None]
    for operation, data in zip(
        case["input"]["operations"], case["input"]["data"]
    ):
        if operation == "ParkingSystem":
            solution = Solution(big=data[0], medium=data[1], small=data[2])
            another_solution = AnotherSolution(
                big=data[0], medium=data[1], small=data[2]
            )
        
        else:
            solution_answer.append(solution.addCar(carType=data[0]))
            another_solution_answer.append(
                another_solution.addCar(carType=data[0])
            )
    
    assert case["output"] == solution_answer
    assert case["output"] == another_solution_answer
    