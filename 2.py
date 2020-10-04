# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        now = ListNode()
        ans = now
        jin = 0
        while l1 and l2:
            s = l1.val + l2.val + jin
            jin = s // 10
            s = s % 10
            
            now.next = ListNode(s)
            
            now = now.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while jin and l1:
                s = l1.val + jin
                jin = s // 10
                s = s % 10
                now.next = ListNode(s)
                now = now.next
                l1 = l1.next
            now.next = l1
        elif l2:
            while jin and l2:
                s = l2.val + jin
                jin = s // 10
                s = s % 10
                now.next = ListNode(s)
                now = now.next
                l2 = l2.next
            now.next = l2
        if jin:
            now.next = ListNode(jin)
            

        return ans.next
