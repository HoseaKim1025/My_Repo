# A B C D E 중 최소 2명 이상의 경우의 수
cnt = 0
ans = 0
for i in range(1 << 5):
    cnt = 0
    for j in range(5):
        if i & (1 << j):
            cnt += 1
    if cnt >= 2:
        ans += 1
print(ans)
