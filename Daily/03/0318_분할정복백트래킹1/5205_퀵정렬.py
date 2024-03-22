# 3월 18일 <병합정복, 백트래킹> 5205 퀵 정렬
def q_sort(arr, L, R):
    if L < R:
        pivot = partition(arr, L, R)
        q_sort(arr, L, pivot-1)
        q_sort(arr, pivot+1, R)


def partition(arr, L, R):
    p = arr[L]
    i, j = L, R
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[L], arr[j] = arr[j], arr[L]
    return j


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    q_sort(arr, 0, n-1)

    print(f'#{case}', arr[n//2])

# n = 8
# arr = [69, 10, 30, 2, 16, 8, 31, 22]
# q_sort(arr, 0, n - 1)
# print(arr)
