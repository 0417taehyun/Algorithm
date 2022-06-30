# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 문자열 압축

def solution(s: str) -> int:
    answer: int = len(s)
    for jump_idx in range(1, (len(s) // 2) + 1):
        count: int = 0
        result_string: str = ""
        previous_string: str = s[:jump_idx]
        for idx in range(0, len(s), jump_idx):
            target_string: str = s[idx:idx+jump_idx]

            if target_string == previous_string:
                count += 1
            
            else:
                result_string += previous_string
                if count != 1:
                    result_string += str(count)
                
                count = 1
                previous_string = target_string
        
        result_string += previous_string
        if count != 1:
            result_string += str(count)
        
        if answer > len(result_string):
            answer = len(result_string)

    return answer


if __name__ == "__main__":
    cases: list[dict[str, str | int]] = [
        {"s": "aabbaccc", "output": 7},
        {"s": "ababcdcdababcdcd", "output": 9},
        {"s": "abcabcdede", "output": 8},
        {"s": "abcabcabcabcdededededede", "output": 14},
        {"s": "xababcdcdababcdcd", "output": 17},
    ]
    for case in cases:
        assert case["output"] == solution(s=case["s"])
        