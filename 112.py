# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        val = sum - root.val
        if  val == 0:
            if not (root.left or root.right):
                return True
            

        if self.hasPathSum(root.left, val):
            return True

        if self.hasPathSum(root.right, val):
            return True
        else:
            return False
