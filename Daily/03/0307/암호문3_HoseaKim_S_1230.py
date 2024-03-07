# 암호문3 swea 1230
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


for case in range(1, 11):
    n = int(input())
    password = list(input().split())
    m = int(input())
    command = list(input().split())

    head = ListNode(password[0])
    curr_node = head

    for i in range(1, n):
        curr_node.next = ListNode(password[i])
        curr_node = curr_node.next

    i = 0
    while i < len(command):
        if command[i] == 'I':
            x, y = int(command[i+1]), int(command[i+2])
            if x == 0:
                new_head = ListNode(command[i+3])
                new_node = new_head
                for j in range(1, y):
                    new_node.next = ListNode(command[i+3+j])
                    new_node = new_node.next
                new_node.next = head
                head = new_head
            else:
                node = head
                cnt = 1
                while cnt < x:
                    node = node.next
                    cnt += 1
                next_node = node.next
                for j in range(y):
                    node.next = ListNode(command[i+3+j])
                    node = node.next
                node.next = next_node
            i += 3 + y
        elif command[i] == 'D':
            x, y = int(command[i+1]), int(command[i+2])
            node = head
            cnt = 1
            while cnt < x:
                node = node.next
                cnt += 1
            next_node = node.next
            for j in range(y):
                next_node = next_node.next
            node.next = next_node
            i += 3
        elif command[i] == 'A':
            y = int(command[i+1])
            for j in range(y):
                curr_node.next = ListNode(command[i+2+j])
                curr_node = curr_node.next
            i += 2 + y

    print(f'#{case}', end=' ')

    node = head
    for _ in range(10):
        print(node.val, end=' ')
        node = node.next
    print()
