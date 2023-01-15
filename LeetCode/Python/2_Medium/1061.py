# [ LeetCode ] 1061. Lexicographically Smallest Equivalent String

class UnionFind:
    def __init__(self, size: int) -> None:
        self.root: list[int] = [ vertex for vertex in range(size) ]

    def find(self, vertex: int) -> int:
        if vertex == self.root[vertex]:
            return vertex
        self.root[vertex] = self.find(vertex=self.root[vertex])
        return self.root[vertex]

    def union(self, u: int, v: int) -> None:
        u_root: int = self.find(vertex=u)
        v_root: int = self.find(vertex=v)
        if u_root != v_root:
            if u_root < v_root:
                self.root[v_root] = u_root
            else:
                self.root[u_root] = v_root


def solution(s1: str, s2: str, baseStr: str) -> str:
    answer: list[str] = []
    START: int = ord('a')
    END: int = ord('z')
    union_find: UnionFind = UnionFind(size=END-START+1)
    for u, v in zip(s1, s2):
        union_find.union(u=ord(u)-START, v=ord(v)-START)
    for target in baseStr:
        root: str = chr(union_find.find(vertex=ord(target)-START)+START)
        answer.append(root)
    return "".join(answer)
