def word_puzzle(n, k, arr):
    word_cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt_x = 1
                cnt_y = 1
                # print('arr :', i, j)
                if 0 <= i-1 and arr[i-1][j] == 1:
                    pass
                else:
                    for x in range(i+1, n):
                        if arr[x][j] == 1:
                            cnt_x += 1
                        else:
                            break
                    # print('cnt_x :', cnt_x)
                    if cnt_x == k:
                        word_cnt += 1
                        # print('x', word_cnt)
                if 0 <= j-1 and arr[i][j-1] == 1:
                    pass
                else:
                    for y in range(j+1, n):
                        if arr[i][y] == 1:
                            cnt_y += 1
                        else:
                            break
                    # print('cnt_y :', cnt_y)
                    if cnt_y == k:
                        word_cnt += 1
                        # print('y', word_cnt)
    
    return word_cnt


T = int(input())
for case in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case} {word_puzzle(n, k, arr)}')