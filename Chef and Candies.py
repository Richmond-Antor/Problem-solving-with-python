t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    if n > x:
        a = n - x
        b = (a + 3) // 4
        print(b)
    else:
        print(0)
