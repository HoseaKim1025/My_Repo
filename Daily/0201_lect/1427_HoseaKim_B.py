# 1. sort 함수 사용
n = list(input())

n.sort(reverse=True)
n = ''.join(n)

print(n)


# # 2. 버블 정렬
# n = list(input())
#
# n_len = len(n)
# for i in range(n_len-1):
#     for j in range(i+1, n_len):
#         if n[i] < n[j]:   # 내림차순
#             n[i], n[j] = n[j], n[i]
#
# print(''.join(n))


# # 3. 카운팅 정렬
#
# n = list(map(int, input()))
#
# n_len = len(n)
# cnt = [0] * 10          # 한 자리수마다 값이 0~9 이므로
# for i in range(n_len):  # n의 길이만큼
#     cnt[n[i]] += 1
#
# for i in range(1, 10):  # 1~9
#     cnt[i] += cnt[i-1]
#
# temp = [0] * n_len       # n의 길이만큼
# for i in range(n_len):  # n의 길이만큼
#     cnt[n[i]] -= 1
#     temp[n_len-1 - cnt[n[i]]] = n[i]
#
# ans = list(map(str, temp))
# print(''.join(ans))


# # 4. 선택 정렬
#
# n = list(input())
#
# n_len = len(n)
# for i in range(n_len-1, 0, -1):
#     min_idx = i
#     for j in range(i-1, -1, -1):
#         if n[min_idx] > n[j]:
#             min_idx = j
#     n[i], n[min_idx] = n[min_idx], n[i]
#
# print(''.join(n))
