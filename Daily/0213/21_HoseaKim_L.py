# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val <= node2.val:
                new_node = node1
                new_node.next = node2
                print('node1 :', node1.val, new_node.val, new_node.next.val)
                next_new_node = new_node.next.next
            elif node2.val < node1.val:
                new_node = node2
                new_node.next = node1
                print('node2 :', node2.val, new_node.val, new_node.next.val)
                next_new_node = new_node.next.next
            node1 = node1.next
            node2 = node2.next
        return


list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
a = Solution()
print(a.mergeTwoLists(list1, list2))
