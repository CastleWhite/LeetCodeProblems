# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        def addSon(node: TreeNode, fatherSum: int) -> int:
            ans = 0
            if node.left:
                ans += addSon(node.left, fatherSum*10+node.val)
            if node.right:
                ans += addSon(node.right, fatherSum*10+node.val)
            if ans:
                return ans
            else:
                return fatherSum*10+node.val
        
        return addSon(root,0)
