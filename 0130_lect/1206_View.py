# import sys
# sys.stdin = open('input_view.txt', 'r')

T = 10
for case in range(1, T+1):
    n = int(input())
    buildings = list(map(int, input().split()))

    view_total = 0
    for i in range(2, len(buildings)-2):
        near_list = []
        for j in [-2, -1, 1, 2]:
            # print(f'{i}: {buildings[i+j]}')
            if buildings[i+j] >= buildings[i]:
                # print('break')
                break
            else:
                near_list.append(buildings[i+j])
                # print(near_list)
        else:
            # print(max(near_list))
            view_total += buildings[i] - max(near_list)
    print(f'#{case} {view_total}')

'''
10
0 0 10 5 8 2 5 7 0 0
'''