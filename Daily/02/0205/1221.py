# import sys
# sys.stdout = open('stdout.txt', 'w')

def gns(list_len, str_list):

    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = {}
    for i in num:
        cnt[i] = 0
    for i in range(list_len):
        cnt[str_list[i]] += 1
    for i in range(1, 10):
        cnt[num[i]] += cnt[num[i-1]]

    temp = [0] * list_len
    for i in range(list_len):
        cnt[str_list[i]] -= 1
        temp[cnt[str_list[i]]] = str_list[i]

    return temp


T = int(input())
for case in range(1, T+1):
    test_case, list_len = input().split()
    str_list = list(map(str, input().split()))

    ans = gns(int(list_len), str_list)
    print(f'#{case}')
    print(*ans)

# sys.stdout.close()
