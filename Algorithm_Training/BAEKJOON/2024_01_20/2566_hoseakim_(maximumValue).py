mat = [list(map(int, input().split())) for _ in range(9)]
max_list = []
column_list = []
for i in range(9):
    max_list.append(max(mat[i]))
    column_list.append(mat[i].index(max(mat[i])))
Max = max(max_list)
row = max_list.index(Max)
column = column_list[row]
print(f'{Max}\n{row+1} {column+1}')