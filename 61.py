# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next: return head
        p = head
        i = 1
        l = 1
        while i < k:
            if p.next:
                i += 1
                p = p.next
            else:
                l = i
                break
        if i < k:
            k = k % l
            if k == 0: return head
            i = 1
            p = head
            while i < k:
                i += 1
                p = p.next
        if not p.next: return head
        pre = ListNode(0, head)
        while p.next:
            p = p.next
            pre = pre.next
        newhead = pre.next
        p.next = head
        pre.next = None
        return newhead
