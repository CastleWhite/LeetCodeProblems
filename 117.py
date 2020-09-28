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
        layer = root
        while layer:
            thr = Node()
            thr = layer
            first = None
            while thr:
                if thr.left:
                    first = thr.left
                    break
                if thr.right:
                    first = thr.right
                    break
                thr = thr.next
            front = Node()    
            while thr:
                if thr.left:
                    front.next = thr.left
                    front = thr.left
                if thr.right:
                    front.next = thr.right
                    front = thr.right
                thr = thr.next
            layer = first

        return root
            

            
