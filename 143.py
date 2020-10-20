# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        l = []
        a = head
        while a:
            l.append(a)
            a = a.next

        a = head
        for i in range((len(l)-1) // 2):
            l[-1-i].next = a.next
            a.next = l[-1-i]
            a = a.next.next
        l[-1-((len(l)-1) // 2)].next = None
 ## 中点、反转、合并
