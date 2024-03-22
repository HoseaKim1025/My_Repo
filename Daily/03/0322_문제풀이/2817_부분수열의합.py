def combination(i, ss):
    if ss == K:
        global cnt
        cnt += 1
        return
    if i == N or ss > K:
        return
    combination(i+1, ss+arr[i])
    combination(i+1, ss)


T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    combination(0, 0)

    print(f'#{case}', cnt)
