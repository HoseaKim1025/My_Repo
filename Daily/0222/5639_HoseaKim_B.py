# 이진 검색 트리
import sys
input = sys.stdin.readline

node_list = [0] * 10001
top = -1
while True:
    try:
        top += 1
        node_list[top] = int(input())
    except ValueError:
        node_list[-1] = 10**6
        break


def binary_search_tree(i, front):
    global rear
    if node_list[front] > node_list[rear]:
        tree[i*2] = node_list[rear]
        rear += 1
        binary_search_tree(i*2, rear-1)
    if node_list[front] < node_list[rear] < node_list[front - 1]:
        tree[i*2+1] = node_list[rear]
        rear += 1
        binary_search_tree(i*2 + 1, rear-1)

    # tree[i] = node_list[rear]
    # rear += 1
    # a1 = node_list[rear]
    # a2 = node_list[rear-1]
    # binary_search_tree(i*2, rear-1)
    # a1 = node_list[rear]
    # a2 = node_list[front]
    # binary_search_tree(i*2+1, front)


tree = [0] * 10001
tree[1] = node_list[0]
rear = 1
binary_search_tree(1, 0)
