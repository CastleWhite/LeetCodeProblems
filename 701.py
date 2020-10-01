# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        now = root
        while 1:
            if now.val > val:
                if now.left:
                    now = now.left
                else:
                    now.left = TreeNode(val)
                    break
            elif now.val < val:
                if now.right:
                    now = now.right
                else:
                    now.right = TreeNode(val)
                    break
            
        return root
