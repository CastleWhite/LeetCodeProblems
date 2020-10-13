# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         selfval. = x
#         self.left = None
#         self.right = None

class Solution:
    pre = -1
    dMin = float('inf')
    ## !!!
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        def midOrder(root: TreeNode):
            if not root:
                return 
            else:
                midOrder(root.left)
                if self.pre != -1:
                    self.dMin = min(root.val - self.pre, self.dMin)
                self.pre = root.val
                midOrder(root.right)
                return

        midOrder(root)
        return self.dMin
