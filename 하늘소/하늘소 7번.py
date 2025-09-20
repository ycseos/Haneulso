def solve():
    import sys
    input = sys.stdin.readline
    
    INF = int(1e9)
    
    n, m = map(int, input().split())
    
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        dist[a][b] = 1
        dist[b][a] = 1

    x, k = map(int, input().split())
    
    //플로이드 워셜
    for via in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])

    result = dist[1][x] + dist[x][k]
    if result >= INF:
        print(-1)
    else:
        print(result)


if __name__ == "__main__":
    solve()

