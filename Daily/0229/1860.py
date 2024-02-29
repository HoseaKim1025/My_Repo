# 진기의 최고급 붕어빵
T = int(input())
for case in range(1, T+1):
    # 손님 n명, 생산량 (k개/m초)
    n, m, k = map(int, input().split())
    # 손님 도착 시간들
    arrival = list(map(int, input().split()))

    arrival.sort()
    sold = 0
    for t in arrival:
        made = (t // m) * k
        sold += 1
        remain = made - sold
        if remain < 0:
            print(f'#{case} Impossible')
            break
    else:
        print(f'#{case} Possible')
