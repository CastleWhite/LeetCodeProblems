# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next

        while even and even.next:
            change = even.next
            odd.next, change.next, even.next = change, odd.next, change.next
            odd = change
            even = even.next

        return head
