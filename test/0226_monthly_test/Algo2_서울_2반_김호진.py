def algorithm_shooting_game(i):
    global max_score
    # n번째 행까지 모두 순회를 마치고 나면 ~
    if i == n:
        # 0 0, 1 1, ... , n-1 n-1 좌표의 값을 ss에 합산
        # 즉 항상 우하향 대각선으로 합산
        score = 0
        for j in range(n):
            if arr[j][j] < 0:
                return
            score += arr[j][j]
        # 합산 점수가 최대 점수보다 높으면 갱신
        if max_score < score:
            max_score = score
    # 아직 모든 행을 순회하지 않은 경우 ~
    for j in range(i, n):
        # i번 행과 j번 행을 뒤바꿔가며 모든 경우의 행 배치를 구현
        arr[i], arr[j] = arr[j], arr[i]
        algorithm_shooting_game(i+1)
        arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_score = 0
    algorithm_shooting_game(0)

    print(f'#{case}', max_score)

# [1, 2, ... , n] 을 모든 경우의 순열로 배치해 합산 시 적용하여 푸는 방식 대신
# arr의 행을 마치 순열처럼 취급해 풀었습니다.
