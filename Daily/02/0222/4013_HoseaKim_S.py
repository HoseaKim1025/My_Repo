def turn():
    rear = [0, 0, 0, 0]
    for obj_num, d in turn_info:
        n = obj_num - 1
        L, dL = n-1, d
        R, dR = n+1, d

        rear[n] = (rear[n] - d) % 8
        while R < 4:
            if mag_list[R-1][(rear[R-1]+dR+2) % 8] == mag_list[R][(rear[R]-2) % 8]:
                break
            dR = -dR
            rear[R] = (rear[R] - dR) % 8
            R += 1
        while L >= 0:
            if mag_list[L+1][(rear[L+1]+dL-2) % 8] == mag_list[L][(rear[L]+2) % 8]:
                break
            dL = -dL
            rear[L] = (rear[L] - dL) % 8
            L -= 1

    score = 0
    for i in range(4):
        if mag_list[i][rear[i]] == 1:
            score += 2**i

    return score


T = int(input())
for case in range(1, T+1):
    K = int(input())        # 자석 회전 수
    # 자석 4개 각각의 자석 날 8개의 자성 정보
    mag_list = [list(map(int, input().split())) for _ in range(4)]
    # K 개의 돌리는 자석 번호 + 턴 방향(1: 시계, -1: 반시계)
    turn_info = [list(map(int, input().split())) for _ in range(K)]

    print(f'#{case}', turn())
