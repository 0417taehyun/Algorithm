# [ 백준 ] 1092번: 배

def solution() -> None:
    N: int = int(input())
    crains: list[list[int]] = sorted(
        [
            [crain, 0] for crain
            in list(map(int, input().split()))
        ],
        reverse=True
    )
    M: int = int(input())
    boxes: list[int] = sorted(list(map(int, input().split())), reverse=True)

    can_all_boxes_lifted: bool = True
    for box in boxes:
        is_lifted: bool = False
        lift_target_indexes: list[int] = []
        
        for i in range(N):
            if crains[i][0] >= box:
                if crains[i][1] == 0:
                    crains[i][1] += 1
                    is_lifted = True
                    break
            
                else:
                    lift_target_indexes.append(i)
                
        if not is_lifted and crains[0][0] >= box:
            current: int = 10000
            for target_idx in lift_target_indexes:
                if crains[target_idx][1] < current:
                    current = crains[target_idx][1]
                    current_idx = target_idx
                
            crains[current_idx][1] += 1
        
        elif crains[0][0] < box:
            can_all_boxes_lifted = False

    if not can_all_boxes_lifted:
        print(-1)
        
    else:
        print(max(cnt for _, cnt in crains))
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    

    cases: list[dict[str, list[str] | str]] = [
        {
            "input": ["3", "6 8 9", "5", "2 5 2 4 7"],
            "output": "2\n",
        },
        {
            "input": ["2", "19 20", "7", "14 12 16 19 16 1 5"],
            "output": "4\n",
        },
        {
            "input": ["4", "23 32 25 28", "10", "5 27 10 16 24 20 2 32 18 7"],
            "output": "3\n",
        },
        {
            "input": ["10", "11 17 5 2 20 7 5 5 20 7", "5", "18 18 15 15 17"],
            "output": "2\n",
        },
        {
            "input": ["10", "11 17 5 2 20 7 5 5 20 7", "5", "18 18 15 15 21"],
            "output": "-1\n",
        },                               
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        