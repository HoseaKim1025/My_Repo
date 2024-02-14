def operator_add(n, num_list, operator):

    max_num = 0
    semi_max_num = 0
    for i in range(n):
        if max_num < num_list[i]:
            max_num = num_list[i]
        elif semi_max_num < num_list[i]:
            semi_max_num = num_list[i]


    return


n = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))

print(operator_add(n, num_list, operator))
