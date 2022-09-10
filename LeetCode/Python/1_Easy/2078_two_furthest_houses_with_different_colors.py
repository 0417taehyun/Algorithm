# [ LeetCode ] 2078. Two Furthest Houses With Different Colors

def solution(colors: list[int]) -> int:
    colors_indexes: dict[int, list[int]] = {}
    for idx, color in enumerate(colors):
        if color in colors_indexes:
            colors_indexes[color][1] = idx
        else:
            colors_indexes[color] = [idx, idx]
    
    from_first: list[list[int]] = sorted(
        colors_indexes.values(), key=lambda x: x[0]
    )
    from_last: list[list[int]] = sorted(
        colors_indexes.values(), key=lambda x: x[1], reverse=True
    )
    if from_first[0] == from_last[0]:
        return max(
            from_last[0][1] - from_first[1][0],
            from_last[1][1] - from_first[0][0]
        )
        
    else:
        return from_last[0][1] - from_first[0][0]


def another_solution(colors: list[int]) -> int:
    def find_different_color(
        target: int, start: int, last: int, reverse: int
    ) -> int:
        for idx in range(start, last, reverse):
            if colors[idx] != target:
                return idx
        
        return -1         
    
    
    length: int = len(colors)
    if colors[0] == colors[-1]:
        middle: int = length // 2
        from_left: int = find_different_color(
            target=colors[0], start=0, last=middle, reverse=1
        )
        from_right: int = find_different_color(
            target=colors[0], start=length-1, last=middle-1, reverse=-1
        )
        if from_left == -1:
            return from_right
        elif from_right == -1:
            return length - 1 - from_left
        else:
            return max(length - 1 - from_left, from_right)
    
    else:
        return length - 1


def simple_solution(colors: list[int]) -> int:
    answer: int = 0
    first_color, last_color = colors[0], colors[-1]
    for idx, color in enumerate(colors):
        if color != first_color:
            answer = max(answer, idx)
        if color != last_color:
            answer = max(answer, len(colors) - 1 - idx)
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": { "colors": [1, 1, 1, 6, 1, 1, 1] },
            "output": 3
        },
        {
            "input": { "colors": [1, 8, 3, 8, 3] },
            "output": 4
        },
        {
            "input": { "colors": [0, 1] },
            "output": 1
        },
        {
            "input": {
                "colors": [4, 4, 4, 11, 4, 4, 11, 4, 4, 4, 4, 4]
            },
            "output": 8
        }                        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        assert case["output"] == simple_solution(**case["input"])
        