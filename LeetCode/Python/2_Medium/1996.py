# [ LeetCode ] 1996. The Number of Weak Characters in the Game

def solution(properties: list[list[int]]) -> int:
    properties.sort(key=lambda x: (-x[0], x[1]))
    maximum_defense: int = properties[0][1]
    
    answer: int = 0
    for _, defense in properties:
        if defense < maximum_defense:
            answer += 1 
        else:
            maximum_defense = defense
    
    return answer


def another_solution(properties: list[list[int]]) -> int:
    maximum_attack: int = 0
    for attack, _ in properties:
        if attack > maximum_attack:
            maximum_attack = attack
    
    bucket: list[int] = [ 0 for _ in range(maximum_attack+2) ]
    for attack, defense in properties:
        if bucket[attack] < defense:
            bucket[attack] = defense
    
    for idx in range(maximum_attack+1, 0, -1):
        if bucket[idx] > bucket[idx-1]:
            bucket[idx-1] = bucket[idx]
    
    answer: int = 0
    for attack, defense in properties:
        if defense < bucket[attack+1]:
            answer += 1
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, list[list[int]] | int]] = [
        {
            "input": { "properties": [[5, 5],[6, 3],[3, 6]] },
            "output": 0
        },
        {
            "input": { "properties": [[2, 2],[3, 3]] },
            "output": 1
        },
        {
            "input": { "properties": [[1, 5],[10, 4],[4, 3]] },
            "output": 1
        },
        {
            "input": { "properties": [[1, 1],[2, 1],[2, 2],[1, 2]] },
            "output": 1
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
