# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        pre = head.val
        p = head
        while p.next:
            if p.next.val == pre:
                p.next = p.next.next
            else:
                pre = p.next.val
                p = p.next

        return head
