# 소프티어 로봇이 지나간 경로 (Lv.3)
import sys
input = sys.stdin.readline

def dfs(i, j, init_d, remain, cnt):
    global min_cnt, max_command, flag

    if min_cnt <= cnt:
        return

    if remain == 0:
        if min_cnt > cnt:
            min_cnt = cnt
            max_command = stack[:]
            flag = 1
        return

    for k in [0, 1, -1, 2]:
        d = (init_d + k) % 4

        ni, nj = i + dx[d], j + dy[d]
        if 0 <= ni < H and 0 <= nj < W and \
                arr[ni][nj] == '#' and visited[ni][nj] == 0:

            nni, nnj = ni + dx[d], nj + dy[d]
            if 0 <= nni < H and 0 <= nnj < W and \
                    arr[nni][nnj] == '#' and visited[nni][nnj] == 0:

                visited[ni][nj] = visited[nni][nnj] = 1
                stack.extend(command[k])

                dfs(nni, nnj, d, remain-2, cnt+1+abs(k))

                visited[ni][nj] = visited[nni][nnj] = 0
                for _ in range(1+abs(k)):
                    stack.pop()


H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]

direction = ('>', 'V', '<', '^')
command = {0: 'A', 1: ['R', 'A'], -1: ['L', 'A'], 2: ['R', 'R', 'A']}
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)

amount = 0
path = []
for i in range(H):
    for j in range(W):
        if arr[i][j] == '#':
            amount += 1
            path.append([i, j])

min_cnt = 10**9
max_command = []
max_idx = [-1, -1, -1]
visited = [[0] * W for _ in range(H)]
for i, j in path:
    for init_d in range(4):
        visited = [[0] * W for _ in range(H)]
        stack = []
        flag = 0
        visited[i][j] = 1
        dfs(i, j, init_d, amount-1, 0)
        visited[i][j] = 0
        if flag:
            max_idx = [i, j, init_d]

print(max_idx[0]+1, max_idx[1]+1)
print(direction[max_idx[2]])
print(*max_command, sep='')
