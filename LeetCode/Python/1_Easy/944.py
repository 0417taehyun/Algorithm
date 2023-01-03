# [ LeetCode ] 944. Delete Columns to Make Sorted

def solution(strs: list[str]) -> int:
    answer: int = 0
    for column in range(len(strs[0])):
        previous_character: str = strs[0][column]
        for row in range(1, len(strs)):
            if previous_character > strs[row][column]:
                answer += 1
                break
            previous_character = strs[row][column]

    return answer
    