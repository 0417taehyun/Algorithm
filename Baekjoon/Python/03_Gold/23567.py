def solution() -> None:
    from collections import defaultdict
    
    
    n, k = map(int, input().split())
    P = [ int(input()) for _ in range(n) ]
    
    start, end = 0, 0
    colors: dict[int, int] = defaultdict(int)
    for index, color in enumerate(P):
        if color in colors:
            if color == P[start]:
                start += 1
                
            else:
                colors[color] += 1
        
        if len(colors) == k:
            end = index
            break
    
    answer: int = 0
    if end != 0:
        window: int = end - start + 1
        while (window > k) and (end < n):
            if P[end] == P[start]:
                start += 1
            else:
                end += 1
                
            
            start_color: int = P[start]
            if colors[start_color] in colors and colors[start_color] > 1:
                
            colors[start] -= 1
            start += 1
            end += 1
            