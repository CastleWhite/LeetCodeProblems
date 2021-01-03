# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smallHead = ListNode()
        bigHead = ListNode()

        smallTail = smallHead
        bigTail = bigHead
        cur = head

        while cur:
            if cur.val < x:
                smallTail.next = cur
                smallTail = smallTail.next
            else:
                bigTail.next = cur
                bigTail = bigTail.next
            cur = cur.next

        smallTail.next = bigHead.next
        bigTail.next = None
        return smallHead.next
