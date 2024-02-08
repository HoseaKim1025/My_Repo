def paper(n):
    ans = 1
    cnt = 1
    while cnt < n//10:
        cnt += 1
        if cnt % 2 == 0:
            ans = ans * 2 + 1
        else:
            ans = ans * 2 - 1

    return ans


T = int(input())
for case in range(1, T+1):
    n = int(input())

    print(f'#{case}', paper(n))
