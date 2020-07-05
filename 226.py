# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode :
        if not root:
            return None
        r = self.invertTree(root.left)
        l = self.invertTree(root.right)    
        root.left = l
        root.right = r 
        return root
