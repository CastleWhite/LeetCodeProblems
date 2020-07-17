# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        slow = head
        for i in range(k-1):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow
