# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        def cut(head, length):
            p = head
            length -= 1
            while p and length:
                length -= 1
                p = p.next
            if p:
                tmp = p
                p = p.next
                tmp.next = None
            return p

        def merge(left, right):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            tail.next = left if left else right
            while tail.next: tail = tail.next

            return dummy.next, tail

        # count length
        l = 0
        p = head
        while p:
            l += 1
            p = p.next

        dummy = ListNode(next = head)
        subL = 1
        while subL < l:
            cur = dummy.next
            tail = dummy

            while cur:
                a = cur 
                b = cut(a, subL)
                if b:
                    cur = cut(b, subL)
                    tail.next, t = merge(a, b)
                    tail = t
                    tail.next = cur
                else:
                    cur = None

            subL *= 2

        return dummy.next
