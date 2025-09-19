from typing import List, Tuple

_MOVE = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

def final_position(n: int, plan: str) -> tuple[int, int]:
    r, c = 1, 1
    for cmd in plan.upper().split():
        if cmd not in _MOVE:
            continue
        dr, dc = _MOVE[cmd]
        nr, nc = r + dr, c + dc
        if 1 <= nr <= n and 1 <= nc <= n:
            r, c = nr, nc
    return r, c

def solve():
    import sys
    input = sys.stdin.readline
    
    n = int(input().strip())     
    plan = input().strip()     
    
    r, c = final_position(n, plan)
    print(r, c)

if __name__ == "__main__":
    solve()
