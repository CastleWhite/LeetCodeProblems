# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if not root: return 
        tail = TreeNode()
        stack = [root]
        while stack:
            n = stack.pop()
            if not n:
                continue
            stack.append(n.right)
            stack.append(n.left)
            tail.right = n
            tail = n
            tail.left = None
