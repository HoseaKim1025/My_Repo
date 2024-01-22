n_in, b_in = input().split()
n_list = list(n_in)
b = int(b_in)
# print(n_list, b)
sum_n = 0
for i in range(len(n_list)):
    if n_list[i].isdecimal:
        # print(n_list[i])
        n_list[i] = int(n_list[i])
        print(n_list[i])
    elif n_list[i].isalpha:
        # print(n_list[i], ord(n_list[i]))
        n_list[i] = ord(n_list[i]) - 55
        print(n_list[i])
    sum_n += n_list[i] * b**(len(n_list) - i)
    # print(sum_n)
print(sum_n)
# sum_n = 0
# for i in range(len(n_list)-1, -1, -1):
#     sum_n += n_list[i] * b**
# print(sum_n)



# print(n)
# for i in range(len(n)):
#     if n[i].isalpha:
#         n[i] = ord(n[i]) - 55
# real_n = sum(n)
# print(real_n)




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