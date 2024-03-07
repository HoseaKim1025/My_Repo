def string_compare(str1, str2):

    for i in range(len(str2) - len(str1) + 1):
        if str2[i:i+len(str1)] == str1:
            return 1

    return 0


T = int(input())
for case in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f'#{case} {string_compare(str1, str2)}')
