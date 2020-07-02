# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None:
            return q == None
        if q == None:
            return False
        a=p.val 
        b=q.val
        if (a == b):
            return self.isSameTree(p.left ,q.left) and self.isSameTree(p.right ,q.right) 
        else :
            return False

        
