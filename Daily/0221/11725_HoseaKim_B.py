# 트리의 부모 찾기
def preorder_traversal(i):

    for j in range(len(tree_dict[i])):
        if not(tree_dict[i][j] == 1 or par[tree_dict[i][j]]):
            par[tree_dict[i][j]] = i
            preorder_traversal(tree_dict[i][j])


N = int(input())
info_list = [list(map(int, input().split())) for _ in range(N-1)]

k = list(range(1, N+1))
v = [[] for _ in range(N)]
tree_dict = dict(zip(k, v))
for i in range(N-1):
    tree_dict[info_list[i][0]].append(info_list[i][1])
    tree_dict[info_list[i][1]].append(info_list[i][0])

par = [0] * (N+1)
preorder_traversal(1)

print(*par[2:], sep='\n')
