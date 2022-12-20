# [ LeetCode ] 841. Keys and Rooms

def solution(rooms: list[list[int]]) -> bool:
    count: int = 0
    graph: dict[int, set[int]] = {
        room: set(keys) for room, keys in enumerate(rooms)
    }
    visited: set[int] = set()
    for room, keys in graph.items():
        if room not in visited:
            count += 1
            if count == 2:
                return False
            visited.add(room)
            while keys:
                key: int = keys.pop()
                visited.add(key)
                target_keys: set[int] = graph[key] - visited
                for target_key in target_keys:
                    visited.add(target_key)
                    keys.add(target_key)
    return True


def another_solution(rooms: list[list[int]]) -> bool:
    visited: list[bool] = [ False for _ in range(len(rooms)) ]
    stack: list[list[int]] = [ rooms[0] ]
    visited[0]: bool = True
    while stack:
        keys: int = stack.pop()
        for key in keys:
            if not visited[key]:
                visited[key]: bool = True
                stack.append(rooms[key])
    return all(visited)


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[list[int]]] | bool]] = [
        {
            "input": { "rooms": [[1], [2], [3], []] },
            "output": True
        },
        {
            "input": { "rooms": [[1, 3], [3, 0, 1], [2], [0]] },
            "output": False
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
