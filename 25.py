# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def countK(head):
            for i in range(k-1):
                head = head.next
                if not head:
                    return head
            return head
        dummy = ListNode(0, head)
        pre = dummy
        while head:
            tail = countK(head)
            if not tail: break
            have = head
            ing = head.next
            have.next = tail.next
            for i in range(k-1):
                to = ing.next
                ing.next = have
                have = ing
                ing = to
            pre.next = have
            pre = head
            head = head.next
        return dummy.next
