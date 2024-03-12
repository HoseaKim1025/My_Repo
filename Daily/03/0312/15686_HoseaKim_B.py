# 백준 15686 치킨 배달 (골드5)
def combination(i, cnt):
    global ans
    if cnt == 3:
        ss = 0
        for x in range(len(house)):
            hi, hj = house[x]
            min_distance = 100
            for y in range(len(chicken)):
                ci, cj = chicken[y]
                if bit[y]:
                    distance = abs(hi - ci) + abs(hj - cj)
                    if min_distance > distance:
                        min_distance = distance
            ss += min_distance
        if ans > ss:
            ans = ss
        return
    if i == len(chicken):
        return
    bit[i] = 1
    combination(i+1, cnt+1)
    bit[i] = 0
    combination(i+1, cnt)


# n (2~50), m (1~13)
n, m = map(int, input().split())
# 빈칸0, 집1 (1~2n), 치킨집2 (m~13)
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])

ans = 10**9
bit = [0] * len(chicken)
combination(0, 0)

print(ans)
