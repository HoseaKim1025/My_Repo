# 백준 14500 테트로미노 (골드4)
n, m = map(int, input().split())    # 4 ~ 500
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if i+1 < n and j+1 < m:
            ss = 0
            for x in range(i, i+2):
                for y in range(j, j+2):
                    ss += arr[x][y]
            if ans < ss:
                ans = ss

        si = 0
        if i+2 < n:
            for x in range(i, i+2):
                si += arr[x][j]
            ss = [si] * 6
            if j+1 < m:
                ss[0] += arr[i+2][j] + arr[i+2][j+1]
                ss[1] += arr[i+1][j+1] + arr[i+2][j+1]
                ss[2] += arr[i+2][j] + arr[i+1][j+1]
            if j-1 >= 0:
                ss[3] += arr[i+2][j] + arr[i+2][j-1]
                ss[4] += arr[i+1][j-1] + arr[i+2][j-1]
                ss[5] += arr[i+2][j] + arr[i+1][j-1]
            if ans < max(ss):
                ans = max(ss)

        sj = 0
        if j+2 < m:
            for y in range(j, j+2):
                sj += arr[i][y]
            ss = [sj] * 6
            if i+1 < n:
                ss[0] += arr[i][j+2] + arr[i+1][j+2]
                ss[1] += arr[i+1][j+1] + arr[i+1][j+2]
                ss[2] += arr[i][j+2] + arr[i+1][j+1]
            if i-1 >= 0:
                ss[3] += arr[i][j+2] + arr[i-1][j+2]
                ss[4] += arr[i-1][j+1] + arr[i-1][j+2]
                ss[5] += arr[i][j+2] + arr[i-1][j+1]
            if ans < max(ss):
                ans = max(ss)

        ss = [si, sj]
        if i+3 < n:
            ss[0] += arr[i+2][j] + arr[i+3][j]

        if j+3 < m:
            ss[1] += arr[i][j+2] + arr[i][j+3]

        if ans < max(ss):
            ans = max(ss)

print(ans)