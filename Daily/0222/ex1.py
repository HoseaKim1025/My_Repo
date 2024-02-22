N = int(input())
arr = [[0] * 7, [0] * 7]
print(arr)
for j in range(N-1):
    arr[0][j] = N + j
    arr[1][6-j] = N - j

print(arr)
