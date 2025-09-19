def solve():
    import sys
    input = sys.stdin.readline
    
    n = int(input().strip())
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(", ".join(map(str, dp[:n+1])))


if __name__ == "__main__":
    solve()
