# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            slow = slow.next
            if fast == slow:
                return True

        return False
