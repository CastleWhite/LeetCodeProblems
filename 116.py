"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        father = root
        father2 = root
        while father2.left:
            while father:
                father.left.next = father.right
                if father.next:
                    father.right.next = father.next.left
                father = father.next
            father = father2.left
            father2 = father2.left

        return root
