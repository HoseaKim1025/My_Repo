def f(x, y, max_v):
    # 합산할 장소 ss
    global ss
    # 다음 시작점 초기화
    nx, ny = x, y
    # 시작점부터 m * m 행렬 탐색
    for dx in range(m):
        for dy in range(m):
            ni, nj = x + dx, y + dy
            if 0 <= ni < n and 0 <= nj < n:
                # 최대값 발견 시 최대값 갱신 및 해당 위치를 다음 시작점으로 설정
                if max_v < arr[ni][nj]:
                    max_v = arr[ni][nj]
                    nx, ny = ni, nj
    # 다음 시작점이 현재 시작점과 같으면 탐색 종료
    if nx == x and ny == y:
        # 맨 처음 탐색에서 탐색이 종료됐으면 첫 최대값을 ss에 합산
        if nx == 0 and ny == 0:
            ss += max_v
        return
    # 탐색이 종료되지 않으면 최대값을 ss에 합산한 후 다음 시작점(nx, ny)을 기준으로 재탐색
    ss += max_v
    f(nx, ny, max_v)


T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ss = 0
    # 시작점 : i, j = 0, 0 / 최대값 초기화 = arr[0][0]
    f(0, 0, arr[0][0])

    print(f'#{case}', ss)

# 행렬의 크기가 1 <= M <= N <= 10 이기에, 재귀함수를 써도 충분할 것으로 판단했습니다.
