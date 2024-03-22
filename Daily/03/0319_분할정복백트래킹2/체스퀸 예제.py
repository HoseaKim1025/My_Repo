# 체스 퀸 예제
# 완전탐색으로 기반 만들고 + 가지치기(백트래킹)

# 순열
# 1~3 까지 숫자 배열이 있을 때
# 123, 132, 213, 231, 312, 321

arr = [i for i in range(1, 4)]
path = [0] * 3


def dfs(level):
    # 기저조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복
    if level == 3:
        print(*path)
        return

    # 들어가기 전
    # 다음 재귀 호출
    # - 다음에 갈 수 있는 곳들은 어디인가?
    # - 이 문제에서는 1, 2, 3 세 가지(arr의 길이만큼) 경우의 수가 존재

    # 1. 기본 코드
    # path[level] = arr[0]
    # dfs(level + 1)
    #
    # path[level] = arr[1]
    # dfs(level + 1)
    #
    # path[level] = arr[2]
    # dfs(level + 1)

    # 2. 기본 코드 압축
    # for i in range(len(arr)):
    #     path[level] = arr[i]
    #     dfs(level + 1)

    # 3. 백트래킹 기능 추가
    for i in range(len(arr)):
        # 갈 수 없는 경우를 활용하는 걸 추천
        # 조건 1
        if arr[i] in path:
            continue
        # 조건 2
        # ...

        path[level] = arr[i]
        dfs(level + 1)

        # 갔다와서 할 로직 -> 기존 방문을 초기화
        path[level] = 0


dfs(0)
