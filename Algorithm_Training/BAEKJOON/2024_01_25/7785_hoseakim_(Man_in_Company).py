n = int(input())

# 입력 버전 1 (4044ms)
in_dict = dict(list(input().split()) for _ in range(n))

# 입력 버전 2 (3988ms)
# in_dict = {}
# for _ in range(n):
#     key, value = input().split()
#     in_dict[key] = value

enter_list = []
for key in in_dict.keys():
    if in_dict[key] == 'enter':
        enter_list.append(key)

print(*sorted(enter_list)[::-1], sep='\n' ,end='')