# 스타트와 링크
def team(i):
    start = 0
    link = 0
    global min_diff
    if i == n:
        for j in range(n//2 - 1):
            start += s[p[j]][p[j + 1]] + s[p[j + 1]][p[j]]
        for j in range(n//2, n-1):
            link += s[p[j]][p[j + 1]] + s[p[j + 1]][p[j]]
        if min_diff > abs(start - link):
            min_diff = abs(start - link)
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            team(i+1)
            p[i], p[j] = p[j], p[i]


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

p = list(range(n))
team(0)

print(min_diff)
