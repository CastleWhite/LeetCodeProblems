# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        
        newbegin = dummy
        
        for i in range(left-1):
            newbegin = newbegin.next
        tmphead = newbegin.next
        
        for i in range(right-left):
            lasthead = tmphead.next
            newbegin.next, lasthead.next, tmphead.next = lasthead, newbegin.next, lasthead.next
      
        return dummy.next
