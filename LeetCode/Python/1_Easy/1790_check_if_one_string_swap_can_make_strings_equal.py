# [ LeetCode ] 1790. Check if One String Swap Can Make Strings Equal

def solution(s1: str, s2: str) -> bool:
    first_index, second_index = -1, -1
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            if first_index == -1:
                first_index = index
            elif second_index == -1:
                second_index = index
            else:
                return False
    
    return (
        s1[first_index] == s2[second_index]
        and
        s1[second_index] == s2[first_index]
    )
                    

def another_solution(s1: str, s2: str) -> bool:
    def validate(iter1: list[str], iter2: list[str]) -> bool:
        temp: dict[str, int] = {}
        for character in iter1:
            if character in temp:
                temp[character] += 1
            else:
                temp[character] = 1
        
        for character in iter2:
            if character in temp and temp[character] > 0:
                temp[character] -= 1
            else:
                return False
        
        return True
    
    
    def move_strings(iter1: list[str], iter2: list[str]) -> bool:
        nonlocal swap_count
        characters: dict[str, str] = {}
        for current, target in zip(iter1, iter2):
            if current != target:
                if current in characters:
                    if swap_count > 0:
                        if characters[current] == target:
                            swap_count -= 1
                            characters.pop(current)
                        
                        else:
                            swap_count -= 1
                            characters[target] = characters.pop(current)
                        
                    else:
                        return False
                
                else:
                    characters[target] = current
        
        if characters:
            iter1, iter2 = characters.keys(), characters.values()
            if validate(iter1=iter1, iter2=iter2):
                return move_strings(iter1=iter1, iter2=iter2)
            
            else:
                return False
        
        else:
            return True
    
    
    swap_count: int = 1
    iter1, iter2 = list(s1), list(s2)
    return True if move_strings(iter1=iter1, iter2=iter2) else False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | bool]] = [
        {
            "input": {
                "s1": "bank",
                "s2": "kanb"
            },
            "output": True
        },
        {
            "input": {
                "s1": "attack",
                "s2": "defend"
            },
            "output": False
        },
        {
            "input": {
                "s1": "kelb",
                "s2": "kelb"
            },
            "output": True
        },
        {
            "input": {
                "s1": "ac",
                "s2": "aa"
            },
            "output": False
        },
        {
            "input": {
                "s1": "bca",
                "s2": "abc"
            },
            "output": False
        }                            
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
