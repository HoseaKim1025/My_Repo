def maze(n, arr, start):

    stack = [[start[0], start[1], -1]]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while stack:
        flag = 0
        for d in range(4):
            i = stack[-1][0] + dx[d]
            j = stack[-1][1] + dy[d]
            if (
                0 <= stack[-1][0] + dx[d] < n and
                0 <= stack[-1][1] + dy[d] < n and
                d > stack[-1][2]
            ):
                if arr[stack[-1][0]+dx[d]][stack[-1][1]+dy[d]] == 3:
                    return 1
                elif arr[stack[-1][0]+dx[d]][stack[-1][1]+dy[d]] == 0:
                    stack[-1][2] = d
                    arr[stack[-1][0] + dx[d]][stack[-1][1] + dy[d]] = 1
                    stack.append([stack[-1][0]+dx[d], stack[-1][1]+dy[d], -1])
                    flag = 1
                    break
        if flag == 0:
            stack.pop()

    return 0


def find_start(n, arr):

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return [i, j]


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    start = find_start(n, arr)

    print(f'#{case}', maze(n, arr, start))
