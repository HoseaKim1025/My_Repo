def elec_bus(k, n, m, charge_list):

    station_list = [0] * (n+1)
    for charge in charge_list:
        station_list[charge] += 1

    real_charge = 0
    cnt = 0
    while real_charge + k < n:
        flag = 0
        for i in range(real_charge + k, real_charge, -1):
            if station_list[i] == 1:
                cnt += 1
                real_charge = i
                # print(station_list.index(station_list[i]))
                break
            else:
                flag += 1
            if flag == k:
                return 0
    return cnt


T = int(input())
for line in range(1, T + 1):
    k, n, m = map(int, input().split())
    charge_list = list(map(int, input().split()))
    print(f'#{line} {elec_bus(k, n, m, charge_list)}')
