# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        dummy = ListNode(next = head)
        pre = dummy
        now = pre.next.next
        if pre.next.val == now.val:
            same = True
        else:
            same = False

        while now:
            if now.val == pre.next.val:
                same = True 

            elif same:
                pre.next = now
                same = False
                    
            else:
                pre = pre.next
            now = now.next
        
        if same:
            pre.next = now
        return dummy.next
