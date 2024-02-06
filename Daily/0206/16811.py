def carrot(n, c_list):
    if len(c_list) < 3:
        return -1
    c_list.sort()
    L = n//3
    R = n-n//3
    LL_cnt = 0
    LR_cnt = 0
    RL_cnt = 0
    RR_cnt = 0
    flag = 0
    print(L, n-R)
    print(len(c_list[0:L]), c_list[0:L])
    print(len(c_list[L:R]), c_list[L:R])
    print(len(c_list[R:]), c_list[R:])
    if c_list[L-1] == c_list[L]:
        flag = 1
        while L-1-LL_cnt >= 0 and c_list[L-1-LL_cnt] == c_list[L-1]:
            LL_cnt += 1
        print('LL_cnt :', LL_cnt)
        while L+LR_cnt < n and c_list[L+LR_cnt] == c_list[L]:
            LR_cnt += 1
        print('LR_cnt :', LR_cnt)
        print('L :', L + LR_cnt, R-L + LL_cnt)
        if L + LR_cnt < R-L + LL_cnt:
            L += LR_cnt
        else:
            L -= LL_cnt
    if c_list[R-1] == c_list[R]:
        flag = 1
        while R-1-RL_cnt >= L and c_list[R-1-RL_cnt] == c_list[R-1]:
            RL_cnt += 1
        print('RL_cnt :', RL_cnt)
        while R+RR_cnt < n and c_list[R+RR_cnt] == c_list[R]:
            RR_cnt += 1
        print('RR_cnt :', RR_cnt)
        print('R :', R-L + RR_cnt, n-R + RL_cnt)
        if R-L + RR_cnt < n-R + RL_cnt:
            R += RR_cnt
        else:
            R -= RL_cnt
    if flag == 0 and n % 3 == 2:
        if c_list[L+1] != c_list[L]:
            L += 1
        elif c_list[R-2] != c_list[R-1]:
            R -= 1
    print()
    print(len(c_list[0:L]), c_list[0:L])
    print(len(c_list[L:R]), c_list[L:R])
    print(len(c_list[R:]), c_list[R:])
    box = [c_list[0:L], c_list[L:R], c_list[R:]]
    size_len = [0, 0, 0]
    for i in range(3):
        if box[i] == [] or len(box[i]) > n//2:
            return -1
        else:
            size_len[i] = len(box[i])

    return max(size_len) - min(size_len)


T = int(input())
for case in range(1, T+1):
    n = int(input())    # 당근의 개수
    # n = 30
    c_list = list(map(int, input().split()))    # 당근 크기
    # c_list = list(range(1, 31))
    print(f'#{case} {carrot(n, c_list)}')
