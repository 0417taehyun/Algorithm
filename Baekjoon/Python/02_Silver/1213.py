# [ 백준 ] 1213번: 팰린드롬 만들기

def solution() -> None:
    from collections import defaultdict
    
    
    S: str = input()
    
    total_count: int = 0
    alphas: dict[str, int] = defaultdict(int)
    for alpha in S:
        total_count += 1
        alphas[alpha] += 1
    
    odd_count: int = 0
    even_count: int = 0
    for alpha, count in alphas.items():
        if (count % 2):
            odd_count += 1
        
        else:
            even_count += 1
    
    if (total_count % 2) and (odd_count != 1):
        print("I'm Sorry Hansoo")

    elif not (total_count % 2) and (odd_count != 0):
        print("I'm Sorry Hansoo")
    
    else:
        alphas = sorted(alphas.items(), key=lambda x: x[0])
        
        front_to_end: str = ""
        end_to_front: str = ""
        center_alpha: str = ""
        for alpha, count in alphas:
            if count % 2:
                front_to_end = front_to_end + (alpha * (count // 2))
                end_to_front = (alpha * (count // 2)) + end_to_front
                center_alpha = alpha
            else:
                front_to_end = front_to_end + (alpha * (count // 2))
                end_to_front = (alpha * (count // 2)) + end_to_front

        answer: str = front_to_end + center_alpha + end_to_front
        print(answer)
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    

    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {"input": ["AABB"], "output": "ABBA"},
        {"input": ["AAABB"], "output": "ABABA"},
        {"input": ["ABACABA"], "output": "AABCBAA"},
        {"input": ["ABCD"], "output": "I'm Sorry Hansoo"},
    ]
    for case in cases:
        output: str = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
    