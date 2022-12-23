# [ LeetCode ] 547. Number of Provinces

def solution(is_connected: list[list[int]]) -> int:
    class UnionFind:
        BASE_HEIGHT: int = 1

        def __init__(self, size: int) -> None:
            self.root: list[int] = [ vertex for vertex in range(size) ]
            self.rank: list[int] = [
                UnionFind.BASE_HEIGHT for _ in range(size)
            ]
        
        def find(self, vertex: int) -> int:
            if vertex == self.root[vertex]:
                return vertex
            self.root[vertex]: int = self.find(self.root[vertex])
            return self.root[vertex]
        
        def union(self, u: int, v: int) -> None:
            u_root: int = self.find(u)
            v_root: int = self.find(v)
            if u_root != v_root:
                u_rank: int = self.rank[u_root]
                v_rank: int = self.rank[v_root]
                if u_rank > v_rank:
                    self.root[v_root]: int = u_root
                elif u_rank < v_rank:
                    self.root[u_root]: int = v_root
                else:
                    self.root[v_root]: int = u_root
                    self.rank[u_root] += 1
        
    
    union_find: UnionFind = UnionFind(len(is_connected))
    for i in range(len(is_connected)-1):
        for j in range(i + 1, len(is_connected)):
            if is_connected[i][j] == 1:
                union_find.union(i, j)
    root: set[int] = set()
    for vertex in range(len(is_connected)):
        parent: int = union_find.find(vertex)
        root.add(parent)
    return len(root)


def another_solution(is_connected: list[list[int]]) -> int:
    class UnionFind:
        BASE_HEIGHT: int = 1

        def __init__(self, size: int) -> None:
            self.root: list[int] = [ vertex for vertex in range(size) ]
            self.rank: list[int] = [
                UnionFind.BASE_HEIGHT for _ in range(size)
            ]
            self.count: int = size
        
        def find(self, vertex: int) -> int:
            if vertex == self.root[vertex]:
                return vertex
            self.root[vertex]: int = self.find(self.root[vertex])
            return self.root[vertex]
        
        def union(self, u: int, v: int) -> None:
            u_root: int = self.find(u)
            v_root: int = self.find(v)
            if u_root != v_root:
                u_rank: int = self.rank[u_root]
                v_rank: int = self.rank[v_root]
                if u_rank > v_rank:
                    self.root[v_root]: int = u_root
                elif u_rank < v_rank:
                    self.root[u_root]: int = v_root
                else:
                    self.root[v_root]: int = u_root
                    self.rank[u_root] += 1
                self.count -= 1
        
        def get_connected_components_count(self) -> int:
            return self.count
    
    
    union_find: UnionFind = UnionFind(len(is_connected))
    for i in range(len(is_connected)-1):
        for j in range(i + 1, len(is_connected)):
            if is_connected[i][j] == 1:
                union_find.union(i, j)
    return union_find.get_connected_components_count()    


if __name__ == "__main__":
    cases: list[dict[str, dict[list[list[int]]] | int]] = [
        {
            "input": {
                "is_connected": [
                    [1, 1, 0],
                    [1, 1, 0],
                    [0, 0, 1]
                ]
            },
            "output": 2
        },
        {
            "input": {
                "is_connected": [
                    [1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]
                ]
            },
            "output": 3
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
