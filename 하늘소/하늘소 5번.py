def solve():
    import sys
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    start, end = 0, max(arr)
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for h in arr:
            if h > mid:
                total += h - mid
        
        if total >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(result)


if __name__ == "__main__":
    solve()
