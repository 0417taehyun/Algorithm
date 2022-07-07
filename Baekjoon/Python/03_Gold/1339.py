# [ 백준 ] 1339번: 단어 수학

def failed_solution() -> None:
    N: int = int(input())
    
    alphas: dict[str, dict[str, str | list[int]]] = {}
    for _ in range(N):
        S: str = input()
        length: int = len(S)
        
        for idx, alpha in enumerate(S):
            if alpha in alphas.keys():
                alphas[alpha]["count"] += 1
                alphas[alpha]["index"].append(length-idx)
                alphas[alpha]["index"].sort(reverse=True)
            
            else:
                alphas[alpha] = {"count": 1, "index": [length-idx]}
        
    alphas = sorted(
        alphas.items(),
        key=lambda x: (x[1]["index"][0], x[1]["count"]),
        reverse=True
    )
    
    answer: int = 0
    number: int = 9
    for _, values in alphas:
        for idx in values["index"]:
            answer += 10**(int(idx)-1)*number
        
        number -= 1
    
    print(answer)


def solution() -> None:
    N: int = int(input())
    alphas: dict[str, int] = {}
    for _ in range(N):
        S: str = input()
        length: int = len(S)
        for idx, alpha in enumerate(S):
            value: int = 10**(length-int(idx)-1)
            if alpha in alphas.keys():
                alphas[alpha] += value

            else:
                alphas[alpha] = value
    
    alphas = sorted(alphas.items(), key=lambda x: x[1], reverse=True)

    answer: int = 0
    number: int = 9
    for _, value in alphas:
        answer += (number * value)
        number -= 1
    
    print(answer)
        

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    

    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
            
            return test_stdout.getvalue()
        
    
    cases: list[dict[str, list[str] | int]] = [
        {"input": ['2', "AAA", "AAA"], "output": 1998},
        {"input": ['2', "GCF", "ACDEB"], "output": 99437},
        {
            "input": [
                "10", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            ],
            "output": 45
        },
        {"input": ['2', "AB", "BA"], "output": 187},
        {
            "input": [
                "10", "ABB", "BB", "BB", "BB", "BB",
                "BB", "BB", "BB", "BB", "BB",
            ],
            "output": 1790,
        },
    ]
    for case in cases:
        output: int = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
