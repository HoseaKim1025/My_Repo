'''
#버전1
T = int(input())
for case in range(1, T + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{case}')
    turn = [[] for _ in range(n*n)]
    
    for i in range(n):
        for j in range(n):
            turn[i].append(mat[n-1-j][i])
            turn[n+i].append(mat[n-1-i][n-1-j])
            turn[n*2+i].append(mat[j][n-1-i])
    
    for i in range(n):
        result = ''
        for j in range(n):
            result1 = ''.join(str(s) for s in turn[i+(j*n)])
            result += result1
            if j != n:
                result += ' '
                
        print(result)
'''

#버전2
T = int(input())
for case in range(1, T + 1):
    n = int(input())
    mat = [list(map(str, input().split())) for _ in range(n)]
    print(f'#{case}')
    turn = ['']*(n**2)

    for i in range(n):
        for j in range(n):
            turn[i] += mat[n-1-j][i]
            turn[n+i] += mat[n-1-i][n-1-j]
            turn[n*2+i] += mat[j][n-1-i]

    for i in range(n):
        result = ''
        for j in range(n):
            result += ''.join(turn[i+(j*n)]) + ' '

        print(result)