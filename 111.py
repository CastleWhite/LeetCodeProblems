# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        lmin = self.minDepth(root.left)
        rmin = self.minDepth(root.right)
        if lmin and rmin:
            return min(lmin,rmin)+1
        elif not lmin and not rmin:
            return 1
        elif lmin:
            return lmin+1
        else:
            return rmin+1

        
