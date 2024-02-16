# 큐스택

n = int(input())
a = list(map(int, input().split()))     # data type
b = list(map(int, input().split()))     # data
m = int(input())
c = list(map(int, input().split()))     # insert num

i = n-1
cnt = 0
while i >= 0 and cnt < m:
    if a[i] == 1:
        i -= 1
    else:
        print(b[i], end=' ')
        cnt += 1
        i -= 1

for j in range(m-cnt):
    print(c[j], end=' ')
