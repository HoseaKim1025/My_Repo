# arr = [3, 6, 7, 1, 5, 4]
#
# n = len(arr)
#
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=', ')
#     print()

'''
10
-7 -5 2 3 8 -2 4 6 9
'''


def f(arr, N):
    for i in range(1, 1 << N-1):
        s = 0
        for j in range(N):
            if i & (1 << j):
                # s += arr[j]
                print(arr[j], end=' ')
        print()
    #     if s == 0:
    #         return True
    # return False


N = int(input())
arr = list(map(int, input().split()))
print(f(arr, N))
