from itertools import accumulate


def canEat(candiesCount: list[int], queries: list[list[int]]) -> list[bool]:
    result = []
    prefix = [0] + list(accumulate(candiesCount))

    for query in queries:
        fav, date, max_eat = query
        result.append(
            (prefix[fav] // max_eat) <= date < prefix[fav + 1]
        )
    
    return result


if __name__ == "__main__":
    candiesCount = [5,2,6,4,1]
    queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
    print(canEat(candiesCount, queries))