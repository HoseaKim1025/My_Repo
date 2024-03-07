# 비밀번호 swea 1234
class ListNode:
    def __init__(self, val=0, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


for case in range(1, 11):
    n, password = input().split()
    n = int(n)

    head = ListNode(password[0])
    curr_node = head
    for i in range(1, n):
        curr_node.next = ListNode(password[i])
        curr_node.next.pre = curr_node
        curr_node = curr_node.next

    node = head
    while node.next:
        if node.val != node.next.val:
            node = node.next
        else:
            if node.pre:
                node.pre.next = node.next.next
                if node.next.next:
                    node.next.next.pre = node.pre
                node = node.pre
            else:
                head = node.next.next
                node.next.next.pre = None
                node = head
        if node.pre:
            a0 = node.pre.val
        if node:
            a1 = node.val
        if node.next:
            a2 = node.next.val

    print(f'#{case}', end=' ')

    node = head
    while node:
        print(node.val, end='')
        node = node.next

    print()

