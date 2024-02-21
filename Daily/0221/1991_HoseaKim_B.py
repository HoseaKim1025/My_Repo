# 트리 순회
def preorder_traversal(i):
    ans = chr(i+64)
    print(ans, end='')
    if i in p and L[i]:
        preorder_traversal(L[i])
    if i in p and R[i]:
        preorder_traversal(R[i])


def inorder_traversal(i):
    if i in p and L[i]:
        preorder_traversal(L[i])
    ans = chr(i + 64)
    print(ans, end='')
    if i in p and R[i]:
        preorder_traversal(R[i])


def postorder_traversal(i):
    if i in p and L[i]:
        preorder_traversal(L[i])
    if i in p and R[i]:
        preorder_traversal(R[i])
    ans = chr(i + 64)
    print(ans, end='')


n = int(input())
node_list = [list(input().split()) for _ in range(n)]

p = [0] * (n+1)
L = [0] * (n+1)
R = [0] * (n+1)

for i in range(n):
    par = ord(node_list[i][0]) - 64
    left = ord(node_list[i][1]) - 64
    right = ord(node_list[i][2]) - 64
    if left > 0:
        p[left] = par
        L[par] = left
    if right > 0:
        p[right] = par
        R[par] = right

preorder_traversal(1)
print()
inorder_traversal(1)
print()
postorder_traversal(1)
print()
