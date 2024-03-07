# 두 수의 덧셈 (리트코드 2)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        next = None
        head = ListNode()
        node = head
        first = 0
        now = []
        while l1.val or l1.next or l2.val or l2.next:
            if first:
                node.next = next
                node = node.next
            t = l1.val + l2.val
            node.val += l1.val + l2.val
            if node.val >= 10:
                node.val %= 10
                next = ListNode(1)
            else:
                next = ListNode()
            now.append(node.val)
            if l1.next:
                l1 = l1.next
            else:
                l1 = ListNode()
            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode()
            first = 1
        if next and next.val:
            node.next = next

        while head:
            print(head.val)
            head = head.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
# l1 = ListNode(0)
# l2 = ListNode(0)
# l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
# l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

a = Solution()
a.addTwoNumbers(l1, l2)
