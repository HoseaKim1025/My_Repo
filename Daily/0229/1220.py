# Magnetic
for case in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    '''
    ss = 0
    for j in range(n):
        stack = [0] * n
        top = 0
        for i in range(n):
            if arr[i][j] == 2 and stack[top-1] == 1:
                stack[top] = 2
                top += 1
            elif arr[i][j] == 1 and (stack[top-1] == 2 or stack[0] == 0):
                stack[top] = 1
                top += 1
        ss += top // 2

    print(f'#{case}', ss)
    '''
    ans = 0
    for j in range(n):
        cnt = 0
        is_red = 0
        for i in range(n):
            if arr[i][j] == 1:
                is_red = 1
            elif is_red and arr[i][j] == 2:
                cnt += 1
                is_red = 0
        ans += cnt

    print(f'#{case}', ans)
'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''