def injection():
    



def test(testee):
    for j in range(w):
        pre = -1
        cnt = 0
        for i in range(d):
            if pre == testee[i][j]:
                cnt += 1
                if cnt == 3:
                    break
            else:
                pre = testee[i][j]
                cnt = 0
        else:
            return j
    return 0


T = int(input())
for case in range(1, T+1):
    d, w, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(d)]

    injection()

    print(f'#{case}', )
