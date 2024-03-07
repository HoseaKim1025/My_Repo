def bingo(arr1, arr2):
    i_cnt = [0] * 5     # 가로 빙고 카운트
    j_cnt = [0] * 5     # 세로 빙고 카운트
    ij_cnt = [0, 0]     # 대각 빙고 카운트
    cnt = 0             # 숫자 부른 횟수
    bingo_cnt = 0       # 3이 되면 빙고
    for x in range(5):
        for y in range(5):
            for i in range(5):
                for j in range(5):
                    if arr1[i][j] == arr2[x][y]:
                        cnt += 1

                        i_cnt[i] += 1
                        j_cnt[j] += 1
                        if i == j:
                            ij_cnt[0] += 1
                        if 4-i == j:
                            ij_cnt[1] += 1

                        if i_cnt[i] == 5:
                            bingo_cnt += 1
                            i_cnt[i] = 6
                        if j_cnt[j] == 5:
                            bingo_cnt += 1
                            j_cnt[j] = 6
                        if ij_cnt[0] == 5:
                            bingo_cnt += 1
                            ij_cnt[0] = 6
                        if ij_cnt[1] == 5:
                            bingo_cnt += 1
                            ij_cnt[1] = 6

                        if bingo_cnt >= 3:
                            return cnt


arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]

print(bingo(arr1, arr2))
