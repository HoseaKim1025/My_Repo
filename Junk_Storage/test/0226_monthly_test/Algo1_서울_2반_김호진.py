T = int(input())
for case in range(1, T+1):

    # 돌의 개수, 뒤집기 총 횟수
    n, m = map(int, input().split())

    # 초기 돌 상태
    init = list(map(int, input().split()))

    # m번의 작업 수행
    for _ in range(m):
        # 기준 위치, 작업할 돌의 개수, 수행할 작업 번호
        i, j, w = map(int, input().split())

        # 작업 번호에 따른 작업 수행
        if w == 1:
            # i번째 돌인 i-1부터 +0, +1, ... , +j-1 까지 1번 작업 수행
            for x in range(j):
                if i-1+x < n:
                    if init[i-1+x] == 1:
                        init[i-1+x] = 0
                    else:
                        init[i-1+x] = 1
        elif w == 2:
            # 위와 같이 인덱스에 접근하는 방식으로 2번 작업 수행
            for x in range(j):
                if i-1+x < n:
                    init[i-1+x] = init[i-1]
        elif w == 3:
            # 기준인 i-1 인덱스로부터 +-1, +-2, ... , +-(j) 까지 3번 작업 수행
            for x in range(1, j+1):     # range(1, j)로 하면 +-(j-1)까지만 수행함
                if i-1-x >= 0 and i-1+x < n:
                    if init[i-1-x] == init[i-1+x]:
                        if init[i-1-x] == 1:
                            init[i-1-x] = init[i-1+x] = 0
                        else:
                            init[i-1-x] = init[i-1+x] = 1

    print(f'#{case}', *init)
