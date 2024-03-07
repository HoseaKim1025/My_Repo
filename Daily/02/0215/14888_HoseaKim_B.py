def operator_add(i, p):
    global min_ans
    global max_ans
    if i == n-1:
        print(p)
        temp = num_list[0]
        for j in range(n-1):
            if p[j] == 0:
                temp += num_list[j+1]
            elif p[j] == 1:
                temp -= num_list[j+1]
            elif p[j] == 2:
                temp *= num_list[j+1]
            elif p[j] == 3:
                temp //= num_list[j+1]
        if min_ans > temp:
            min_ans = temp
            print(min_ans)
        if max_ans < temp:
            max_ans = temp
            print(max_ans)
    else:
        for j in range(i, n-1):
            if i != j and p[i] == p[j]:
                continue
            p[i], p[j] = p[j], p[i]
            operator_add(i+1, p)
            p[i], p[j] = p[j], p[i]


def operator_sort(operator):
    p = []
    for i in range(4):
        p += [i] * operator[i]

    return p


n = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
p = operator_sort(operator)
min_ans = int(1e9)
max_ans = int(-1e9)
operator_add(0, p)
print(int(max_ans))
print(int(min_ans))
