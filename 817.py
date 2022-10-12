# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        pre = False
        res = 0
        while (head):
            if head.val in nums:
                pre = True
            else:
                if pre: 
                    res += 1
                    pre = False
            head = head.next
        if pre: res += 1
        return res
