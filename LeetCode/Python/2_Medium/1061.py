# [ LeetCode ] 1061. Lexicographically Smallest Equivalent String

class UnionFind:
    def __init__(self) -> None:
        self.root: dict[str, str] = {
            chr(alphabet): chr(alphabet)
            for alphabet in range(ord('a'), ord('z')+1)
        }

    def find(self, vertex: str) -> str:
        if vertex == self.root.get(vertex):
            return vertex
        self.root[vertex] = self.find(vertex=self.root.get(vertex))
        return self.root.get(vertex)

    def union(self, u: str, v: str) -> None:
        u_root: str = self.find(vertex=u)
        v_root: str = self.find(vertex=v)
        if u_root != v_root:
            if u_root < v_root:
                self.root[v_root] = u_root
            else:
                self.root[u_root] = v_root


def solution(s1: str, s2: str, baseStr: str) -> str:
    answer: list[str] = []
    union_find: UnionFind = UnionFind()
    for u, v in zip(s1, s2):
        union_find.union(u=u, v=v)
    for target in baseStr:
        root: str = union_find.find(vertex=target)
        answer.append(root)
    return "".join(answer)
