# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, node1, node2):
        
        new_single_list = ListNode()
        new_node = new_single_list

        while True:
            if node1.val < node2.val:
                new_node.next = node1
                node1 = node1.next
            elif node2.val < node1.val:
                new_node.next = node2
                node2 = node2.next
            new_node = new_node.next
            if not(node1 or node2):
                break
        
        return new_single_list.next

list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
a = Solution()
print(a.mergeTwoLists(list1, list2))
