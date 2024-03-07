T = int(input())
for case in range(1, T+1):
    n = int(input())
    wire = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if wire[i][0] < wire[j][0]:
                if wire[i][1] > wire[j][1]:
                    cnt += 1
            elif wire[i][0] > wire[j][0]:
                if wire[i][1] < wire[j][1]:
                    cnt += 1

    print(f'#{case}', cnt)
