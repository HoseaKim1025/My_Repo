def min_index(n, num_list):
    for i in range(1, 11):
        for j in range(n):
            if num_list[j] == i:
                return j

def max_index(n, num_list):
    for i in range(10, 0, -1):
        for j in range(n-1, -1, -1):
            if num_list[j] == i:
                return j

T = int(input())
for case in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    Max = max_index(n, num_list)
    Min = min_index(n, num_list)
    print(f'#{case} {abs(Max - Min)}')
