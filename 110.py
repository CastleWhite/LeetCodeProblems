# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root: TreeNode) -> (bool, int):
        if not root:
            return True, 0
        bal, lh = self.height(root.left) 
        if not bal:
            return False, -10

        bal, rh = self.height(root.right) 
        if not bal:
            return False, -10
        
        if abs(lh-rh)>1:
            return False, -10
        else:
            return True, max(lh,rh)+1

    def isBalanced(self, root: TreeNode) -> bool:
        bal ,_ = self.height(root)
        return bal
        
