'''
#노가다 if문
T = int(input())
for case in range(1, T + 1):
    mat = [list(map(int, input().split())) for _ in range(9)]
    brk = False
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if j != k:
                    if mat[i][j] == mat[i][k] or mat[j][i] == mat[k][i]:
                        brk = True
                        print(f'#{case} {0}')
                        break
                elif i%3 == 0 and j%3 == 0 and k%3 == 0:
                    for l in range(3):
                        for m in range(3):
                            for n in range(3):
                                if k != m and l != n:
                                    if mat[k//3+(i//3)*3][l+(j//3)*3] == mat[m+(i//3)*3][n+(j//3)*3]:
                                        brk = True
                                        print(f'#{case} {0}')
                                        break
                            if brk:
                                break
                        if brk:
                            break
            if brk:
                break
        if brk:
            break
    if brk:
        continue
    else:
        print(f'#{case} {1}')
'''
'''
#함수로 풀기
def sudoku(mat):
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if j != k:
                    if mat[i][j] == mat[i][k] or mat[j][i] == mat[k][i]:
                        return 0
                elif i%3 == 0 and j%3 == 0 and k%3 == 0:
                    for l in range(3):
                        for m in range(3):
                            for n in range(3):
                                if k != m and l != n:
                                    if mat[k//3+(i//3)*3][l+(j//3)*3] == mat[m+(i//3)*3][n+(j//3)*3]:
                                        return 0
    return 1

T = int(input())
for case in range(1, T + 1):
    mat = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{case} {sudoku(mat)}')
'''

#set활용하기
def sudoku(mat):
    ref = set(range(1,10))
    for i in range(9):
        if set(mat[i]) != ref:
            return 0
        temp = []
        temp1 = []
        for j in range(9):
            temp.append(mat[j][i])
            if i%3 == 0 and j%3 == 0:
                for k in range(3):
                    for l in range(3):
                        temp1.append(mat[k+(i//3)*3][l+(j//3)*3])
                if set(temp1) != ref:
                    return 0
        if set(temp) != ref:
            return 0
    return 1

T = int(input())
for case in range(1, T + 1):
    mat = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{case} {sudoku(mat)}')
