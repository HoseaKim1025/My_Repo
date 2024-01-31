T = int(input())
for case in range(1, T+1):
    n = int(input())
    rect_list = [list(map(int, input().split())) for _ in range(n)]

    # 10*10 배열에 (0, 0) 생성
    arr = [[[0, 0] for _ in range(10)] for _ in range(10)]

    # 빨간색은 (1, 0)으로 채우고 파란색은 (0, 1)로 채우기
    for rect in rect_list:
        if rect[4] == 1:
            for dx in range(rect[0], rect[2]+1):
                for dy in range(rect[1], rect[3]+1):
                    arr[dx][dy][0] = 1
        if rect[4] == 2:
            for dx in range(rect[0], rect[2]+1):
                for dy in range(rect[1], rect[3]+1):
                    arr[dx][dy][1] = 1

    # 보라색 (1, 1)인 경우를 카운트
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == [1, 1]:
                cnt += 1

    print(f'#{case} {cnt}')
