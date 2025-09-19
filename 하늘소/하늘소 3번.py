from collections import deque

def solve():
    import sys
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
        
        return graph[n-1][m-1]
    
    print(bfs(0, 0))


if __name__ == "__main__":
    solve()
