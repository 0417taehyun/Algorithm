# 평방 분할 (Sqrt Decomposition)

class SqrtDecomposition:
    def __init__(self, array: list[int]) -> None:
        self.array: list[array] = array
        self.block: list[int] = []
        
        block_size: int = int(len(array) ** 0.5)
        element_sum: int = 0
        for index, element in enumerate(array):
            if index == block_size:
                self.block.append(element)
            else:
                element_sum += element
        
        
    def update(self, index: int, value: int) -> None:
        block_idx: int = index % len(self.block)
        self.array[index] = value
        
        
    
    def query(self, start: int, end: int) -> int:
        pass


def solution(N: list[int], start: int, end: int) -> int:
    pass
    

if __name__ == "__main__":
    case: dict[str, dict[str, list[int]] | int] = {
        "input": {
            "N": [ 1, 4, 7, 5, 2, 8, 3, 1, 8, 5, 4, 7, 2, 7, 3, 0 ],
            "start": 4,
            "end": 15,
        },
        "output": 0
    }
    
    assert case["output"] == solution(
        N=case["input"]["N"], start=case["input"]["start"], end=case["input"]["end"]
    )
    