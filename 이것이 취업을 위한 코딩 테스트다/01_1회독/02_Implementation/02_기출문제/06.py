# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 기둥과 보 설치

def validate_structure(answer: list[list[int]]) -> bool:
    for x, y, structure in answer:
        if structure == 0:
            if y == 0:
                pass
            
            elif [x, y-1, 0] in answer:
                pass
            
            elif [x-1, y, 1] in answer:
                pass
            
            elif [x, y, 1] in answer:
                pass
            
            else:
                return False
            
        else:
            if [x, y-1, 0] in answer:
                pass
            
            elif [x+1, y-1, 0] in answer:
                pass
            
            elif ([x-1, y, 1] in answer) and ([x+1, y, 1] in answer):
                pass
            
            else:
                return False
    
    return True


def solution(n: int, build_frame: list[list[int]]) -> list[list[int]]:
    answer: list[list[int]] = []
    
    for x, y, structure, work in build_frame:
        if work == 0:
            answer.remove([x, y, structure])
            if not validate_structure(answer):
                answer.append([x, y, structure])
        
        else:
            answer.append([x, y, structure])
            if not validate_structure(answer):
                answer.remove([x, y, structure])
    
    return sorted(answer)


if __name__ == "__main__":
    cases: list = [
        {
            "n": 5,
            "build_frame": [
                [1,0,0,1], [1,1,1,1], [2,1,0,1], [2,2,1,1],
                [5,0,0,1], [5,1,0,1], [4,2,1,1], [3,2,1,1],
            ],
            "output": [
                [1,0,0], [1,1,1], [2,1,0], [2,2,1],
                [3,2,1], [4,2,1], [5,0,0], [5,1,0],
            ]
        },
        {
            "n": 5,
            "build_frame": [
                [0,0,0,1], [2,0,0,1], [4,0,0,1],
                [0,1,1,1], [1,1,1,1], [2,1,1,1],
                [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1],
            ],
            "output": [ [0,0,0], [0,1,1], [1,1,1], [2,1,1], [3,1,1], [4,0,0] ]
        }
    ]
    for case in cases:
        assert case["output"] == solution(
            n=case["n"], build_frame=case["build_frame"]
        )
