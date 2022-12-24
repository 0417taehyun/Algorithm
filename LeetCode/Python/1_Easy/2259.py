# [ LeetCode ] 2259. Remove Digit From Number to Maximize Result

def solution(number: str, digit: str) -> str:
    latest_index: int = 0
    for idx in range(1, len(number)):
        if number[idx-1] == digit:
            if int(number[idx]) > int(number[idx-1]):
                return number[:idx-1] + number[idx:]
            else:
                latest_index = idx - 1

    if number[-1] == digit:
        return number[:len(number)-1]
    else:
        return number[:latest_index] + number[latest_index+1:]
        

if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | str]] = [
        {
            "input": { "number": "123", "digit": "3" },
            "output": "12"
        },
        {
            "input": { "number": "1231", "digit": "1" },
            "output": "231"
        },
        {
            "input": { "number": "551", "digit": "5" },
            "output": "51"
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        