T = int(input())
for test_case in range(1, T + 1):

    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    for x in range(n):
        for y in range(m-1):
            grid[x].insert(0,0)
            grid[x].append(0)
    extra = [[0]*(n+2*(m-1))]
    grid = extra*(m-1) + grid + extra*(m-1)

    amount = []

    for i in range(m-1, n+m-1): #i,j = 1~2
        for j in range(m-1, n+m-1):
            sum_a = 0
            sum_b = 0
            sum_c = 0
            sum_d = 0
            for k1 in range(j-m+1, j+m):
                a = grid[i][k1]
                sum_a = sum_a + a
            for l1 in range(i-m+1, i+m):
                b = grid[l1][j]
                sum_b = sum_b + b
            amount1 = sum_a + sum_b - grid[i][j]
            for k2 in range(-m+1, m): #k2,l2 = -1~1
                c = grid[i+k2][j+k2]
                sum_c = sum_c + c
            for l2 in range(-m+1, m):
                d = grid[i-l2][j+l2]
                sum_d = sum_d + d
            amount2 = sum_c + sum_d - grid[i][j]
            if amount1 > amount2:
                amount.append(amount1)
            else:
                amount.append(amount2)
                
    result = max(amount)
            
    print(f'#{test_case} {result}')
