# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        red = head.next
        tail = head
        while red:
            if head.val >= red.val:       #使用dummy节点，better？
                tail.next = red.next
                red.next = head
                head = red
            elif tail.val < red.val:
                tail = red

            else:
                find = head
                while find.next.val < red.val:
                    find = find.next
                # if find == tail:
                #     tail = red        提前判断

                tail.next = red.next
                red.next = find.next
                find.next = red

            #insertion finished
            red = tail.next

        return head
