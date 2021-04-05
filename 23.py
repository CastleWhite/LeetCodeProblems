# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        def merge2Lists(list1, list2) -> ListNode:
            head = ListNode()
            tail = head

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
                
            if list2:
                tail.next = list2
            else:
                tail.next = list1
            
            return head.next

        k = len(lists)
        for i in range(ceil(log(k,2))):
            new_lists = []
            while len(lists) > 1:
                list1 = lists.pop()
                list2 = lists.pop()
                new_lists.append(merge2Lists(list1, list2))
            if lists:
                new_lists.append(lists[0])
            lists = new_lists
        
        return lists[0]
