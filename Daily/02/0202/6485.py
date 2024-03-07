import time

def samsung_bus(n, bus_list, p, c_list):

    station = [0] * p
    for i in range(p):
        for bus in bus_list:
            if bus[0] <= c_list[i] <= bus[1]:
                station[i] += 1

    return station

T = int(input())


for case in range(1, T+1):
    n = int(input())    # n : 버스 노선의 개수
    # 버스 노선
    bus_list = [list(map(int, input().split())) for _ in range(n)]
    
    p = int(input())    # p : 정류장의 개수
    # 정류장 번호 나열
    c_list = [int(input()) for _ in range(p)]   
    start = time.time()
    print(f'#{case}', *samsung_bus(n, bus_list, p, c_list))

    end = time.time()
    print(f"{end - start:.5f} sec")