# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next = head)
        toChange = head
        pre = dummy
        while toChange:
            a = toChange
            b = a.next
            if not b: toChange = None
            else:
                toChange = b.next
                pre.next = b
                a.next = toChange
                b.next = a
                pre = a
        return dummy.next
