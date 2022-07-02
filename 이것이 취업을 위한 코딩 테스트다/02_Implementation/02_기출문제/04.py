# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 자물쇠와 열쇠

def validate_lock(M: int, N: int, new_lock) -> list[list[int]]:
    for i in range(N):
        for j in range(N):
            if new_lock[M-1+i][M-1+j] != 1:
                return False
    return True


def rotate(key: list[list[int]]) -> list[list[int]]:
    temp: list[list[int]] = [ [0] * len(key) for _ in range(len(key)) ]
    for i in range(len(key)):
        for j in range(len(key)):
            temp[i][j] = key[j][len(key)-1-i]
    
    return temp


def solution(key: list[list[int]], lock: list[list[int]]) -> bool:
    M: int = len(key)
    N: int = len(lock)

    new_lock: list[list[int]] = [
        [0] * ((M-1)*2 + N) for _ in range(((M-1)*2 + N))
    ]
    for i in range(N):
        for j in range(N):
            new_lock[M-1+i][M-1+j] = lock[i][j]

    answer: bool = False
    for _ in range(4):
        for x in range((M-1)+N):
            for y in range((M-1)+N):
                for i in range(M):
                    for j in range(M):
                        new_lock[i+x][j+x] += key[i][j]
                
                if validate_lock(M, N, new_lock):
                    return True
                
                else:
                    for i  in range(M):
                        for j in range(M):
                            new_lock[i+x][j+x] -= key[i][j]

        key = rotate(key)

    return answer


if __name__ == "__main__":
    cases: list[dict[str]] = [
        {
            "key": [[0, 0, 0], [1, 0, 0], [0, 1, 1]],
            "lock": [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            "output": True
        },
    ]
    for case in cases:
        assert case["output"] == solution(key=case["key"], lock=case["lock"])
