# 역순 연결 리스트 (리트코드 206)
class Solution:
    def reverseList(self, head):
        cur_node = head
        next_node = None
        while cur_node:
            pre_node = cur_node.next
            cur_node.next = next_node
            next_node = cur_node
            cur_node = pre_node

        return next_node