n_in, b_in = input().split()
n_list = list(n_in)
b = int(b_in)
# print(n_list, b)
sum_n = 0
for i in range(len(n_list)):
    if n_list[i].isdecimal():
        n_list[i] = int(n_list[i])
    elif n_list[i].isalpha():
        n_list[i] = ord(n_list[i]) - 55
    sum_n += n_list[i] * b**(len(n_list)-1 - i)
print(sum_n)

# 문제 잘 못 읽고 10진수를 b진수로 바꾸는 코드를 짜버렸는데 지우기 아까워서 남김
# n = int(input())
# b = int(input())
# result = ''
# while True:
#     if n < b*2:
#         n, q = divmod(n, b)
#         if n == 0:
#             if q > 9:
#                 result += chr(65 + q - 10)
#             else:
#                 result += str(q)   
#         else:
#             if q > 9:
#                 result += chr(65 + q - 10)
#             else:
#                 result += str(q) + f'{n}'
#         break
#     n, q = divmod(n, b)
#     if q > 9:
#         result += chr(65 + q - 10)
#     else:
#         result += str(q)

# print(result[::-1])