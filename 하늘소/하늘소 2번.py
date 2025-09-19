import sys


def dfs(x, y, graph, visited, n, m):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0 and not visited[x][y]:
        visited[x][y] = True
        dfs(x-1, y, graph, visited, n, m)
        dfs(x+1, y, graph, visited, n, m)
        dfs(x, y-1, graph, visited, n, m)
        dfs(x, y+1, graph, visited, n, m)
        return True
    return False

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j, graph, visited, n, m):
                count += 1
    print(count)

if __name__ == "__main__":
    solve()
