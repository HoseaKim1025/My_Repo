n = int(input())
num_list = [int(input()) for _ in range(n)]

sig = 0
for num in num_list:
    sig += num

print(round(sig/n))

cnt = [0] * 8001  # -4000 ~ 4000
for num in num_list:
    cnt[num+4000] += 1

most_freq = 0
most_freq_num = -4000
flag = 0
for i in range(8001):
    if most_freq == cnt[i] and flag == 1:
        most_freq_num = i-4000
        flag = 0
    if most_freq < cnt[i]:
        most_freq = cnt[i]
        most_freq_num = i-4000
        flag = 1
    if i > 0:
        cnt[i] += cnt[i-1]

new_list = [0] * n
for num in num_list:
    cnt[num+4000] -= 1
    new_list[cnt[num+4000]] = num

print(new_list[n//2])
print(most_freq_num)
print(new_list[n-1] - new_list[0])