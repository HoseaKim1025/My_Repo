# 화물 토크
T = int(input())
for case in range(1, T+1):
    n = int(input())
    work_time = [list(map(int, input().split())) for _ in range(n)]

    work_time.sort(key=lambda x: (x[1], x[0]))
    end = work_time[0][1]
    i = 0
    cnt = 1
    for i in range(1, n):
        if end <= work_time[i][0]:
            end = work_time[i][1]
            cnt += 1

    print(f'#{case}', cnt)
