T = 10
for case in range(1, T+1):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    s = [0] * 2
    max_s = [0] * 4
    for i in range(100):

        s[0] = s[1] = 0
        for j in range(100):
            s[0] += arr[i][j]
            s[1] += arr[j][i]

        if max_s[0] < s[0]:
            max_s[0] = s[0]
        if max_s[1] < s[1]:
            max_s[1] = s[1]
        max_s[2] += arr[i][i]
        max_s[3] += arr[i][99 - i]

    ans = 0
    for x in range(4):
        if ans < max_s[x]:
            ans = max_s[x]

    print(f'#{case} {ans}')
