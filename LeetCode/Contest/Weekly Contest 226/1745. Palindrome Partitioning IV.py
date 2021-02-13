def checkPartitioning(s: str) -> bool:

    dp = [ [False] * len(s) for _ in range(len(s)) ]
    
    for i in range((len(s) - 1), -1, -1):
        for j in range(len(s)):
            if i >= j:
                dp[i][j] = True
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            
    return dp

if __name__ == "__main__":
    strings = ["abcbdd", "bcbddxy"]

    for s in strings:
        print(checkPartitioning(s))
        