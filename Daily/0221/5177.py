# 이진 힙
def enq(n):

    global last
    last += 1
    h[last] = n
    now = last
    while h[now] < h[now//2]:
        h[now], h[now//2] = h[now//2], h[now]
        now = now//2


T = int(input())
for case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    h = [0] * (N+1)
    last = 0
    for num in num_list:
        enq(num)

    ss = 0
    while last > 1:
        last //= 2
        ss += h[last]

    print(f'#{case}', ss)
