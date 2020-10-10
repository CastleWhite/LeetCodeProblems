# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            slow = slow.next
            if fast == slow:
                a = head
                while a != slow:
                    a = a.next
                    slow = slow.next
                return a
