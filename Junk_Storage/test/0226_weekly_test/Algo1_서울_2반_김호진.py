T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 델타를 이용해 상하좌우를 탐색
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 최대 점수 초기화
    max_score = 0
    # arr 순회
    for i in range(n):
        for j in range(n):
            # 쏜 표적의 점수를 ss에 초기화
            ss = arr[i][j]
            # 델타 방향을 2칸씩 탐색
            for d in range(4):
                for k in range(1, 3):
                    ni = i + dx[d] * k
                    nj = j + dy[d] * k
                    # arr 범위 내에서만 동작 -> ss에 상하좌우 2칸씩 합산
                    if 0 <= ni < n and 0 <= nj < n:
                        ss += arr[ni][nj]
            # 한 표적에 대한 합산이 모두 끝나면 최대 점수 비교 및 갱신
            if max_score < ss:
                max_score = ss

    print(f'#{case}', max_score)
