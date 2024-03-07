def string(str1, str2):
    new_dict = {}
    for i in set(str1):
        new_dict[f'{i}'] = 0
    for i in str2:
        if i in set(str1):
            new_dict[f'{i}'] += 1
    max_cnt = 0
    for i in new_dict.values():
        if max_cnt < i:
            max_cnt = i

    return max_cnt


T = int(input())
for case in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f'#{case} {string(str1, str2)}')
