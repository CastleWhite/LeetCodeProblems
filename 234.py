# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
            
        fast = head
        slow = head
        reco = []
        while fast.next:
            reco.append(slow.val)
            fast = fast.next
            if fast.next:
                fast = fast.next
                slow = slow.next
        
        while slow.next:
            slow = slow.next
            if slow.val != reco.pop():
                return False

        return True
    
    # 修改列表，反转后半，比较，O(1)
            
                
