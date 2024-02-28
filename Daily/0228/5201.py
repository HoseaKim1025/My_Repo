# 컨테이너 운반
T = int(input())
for case in range(1, T+1):
    # 컨테이너 수, 트럭 수
    n, m = map(int, input().split())
    # 컨테이너의 무게
    w = list(map(int, input().split()))
    # 트럭의 적재용량
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)
    # print(w, t)
    ans = 0
    temp = 0
    for j in range(m):
        for i in range(temp, n):
            if t[j] >= w[i]:
                # print(w[i])
                ans += w[i]
                temp = i+1
                break

    print(f'#{case}', ans)
