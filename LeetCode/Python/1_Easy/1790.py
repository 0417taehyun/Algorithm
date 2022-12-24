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
                    

def failure_solution(s1: str, s2: str) -> bool:
    """
    실제 아래 코드로 LeetCode 문제 자체는 풀 수 있지만 확장성 측면에서 실패했다.
    아래는 발견하게 된 엣지 테스트 케이스다.
    
    s1: aabb
    s2: bbaa
    
    위 테스트 케이스처럼 동일한 문자열이 두 개 이상일 때
    해시 테이블은 결국 고유한 키만 가지기 때문에 문제를 해결할 수 없는 자료 구조다.
    """
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
