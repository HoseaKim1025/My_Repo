import time
start = time.time()

n = 10**5
m = 10**9
# t = list(range(1, m, m//n))

t = list(range(1, n+1))
times = [0] * n
sum_times = m * m
temp = m
x = 0
while sum_times != m:
    while sum_times > m:
        for i in range(len(times)):
            times[i] = temp // t[i]
        temp //= 2
        sum_times = sum(times)
    x += times.pop()
    sum_times = sum(times) + x
    print(times[-1])
    print(sum_times)
    temp = m

end = time.time()
print(f'{end - start:.12f} sec')
