from collections import defaultdict


def restoreArray(adjacentPairs: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    for first_num, second_num in adjacentPairs:
        graph[first_num].append(second_num)
        graph[second_num].append(first_num)
        
    for key, value in graph.items():
        if len(value) == 1:
            start_num = key
            break

    nums = []
    seen = set()
    def dfs(num):
        seen.add(num)
        for next_num in graph[num]:
            if not next_num in seen:
                dfs(next_num)
        nums.append(num)
    
    dfs(start_num)
    return nums
    

if __name__ == "__main__":
    adjacentPairs = [[2, 1], [4, 3], [2, 3]]
    print(restoreArray(adjacentPairs))