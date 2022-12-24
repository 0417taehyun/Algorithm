# [ LeetCode ] 1768. Merge Strings Alternately

def solution(word1: str, word2: str) -> str:
    merged_string: list[str] = []
    word1_list: list[str] = list(word1)
    word2_list: list[str] = list(word2)
    
    while word1_list or word2_list:
        if word1_list:
            merged_string.append(word1_list.pop(0))
        
        if word2_list:
            merged_string.append(word2_list.pop(0))
    
    answer: str = "".join(merged_string)
    return answer


def another_solution(word1: str, word2: str) -> str:
    answer: str = ""
    word1_count: int = len(word1)
    word1_index: int = 0
    word2_count: int = len(word2)
    word2_index: int = 0
    
    while word1_index < word1_count or word2_index < word2_count:
        if word1_index < word1_count:
            answer += word1[word1_index]
            word1_index += 1
        
        if word2_index < word2_count:
            answer += word2[word2_index]
            word2_index += 1
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | str]] = [
        {
            "input": {
                "word1": "abc",
                "word2": "pqr"
            },
            "output": "apbqcr"
        },
        {
            "input": {
                "word1": "ab",
                "word2": "pqrs"
            },
            "output": "apbqrs"
        },
        {
            "input": {
                "word1": "abcd",
                "word2": "pq"
            },
            "output": "apbqcd"
        }                
    ]
    for case in cases:
        assert case["output"] == solution(
            word1=case["input"]["word1"],
            word2=case["input"]["word2"]
        )
        assert case["output"] == another_solution(
            word1=case["input"]["word1"],
            word2=case["input"]["word2"]
        )        
    