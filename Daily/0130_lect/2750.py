n = int(input())
num_list = [int(input()) for _ in range(n)]

# 0. sorted() 정렬
# print(*sorted(num_list), sep='\n')

# 1. 버블 정렬
# for i in range(n-1):
#     for j in range(i+1, n):
#         if num_list[i] > num_list[j]:
#             num_list[i], num_list[j] = num_list[j], num_list[i]
# print(*num_list, sep='\n')

# 2. 카운팅 정렬
cnt = [0] * n
for i in range(n):
    cnt[num_list[i]-1] += 1
for j in range(n-1):
    cnt[j+1] += cnt(j)
for k in range(n):

temp =
print(cnt)
