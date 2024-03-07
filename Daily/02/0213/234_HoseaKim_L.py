# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        new_list = []

        node = head
        while node:
            new_list.append(node.val)
            node = node.next
        new_list_len = len(new_list)
        for i in range(new_list_len//2):
            if new_list[i] != new_list[new_list_len-1 - i]:
                return False

        return True


# head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1, next=None))))
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
a = Solution()
print(a.isPalindrome(head))
