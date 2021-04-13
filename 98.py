# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return False
        # 判断中序遍历有序
        def mOrderHelper(root):
            ml = mr = root.val
            if root.left:
                ml, r = mOrderHelper(root.left)
                if ml > r: return 1, 0
                if r >= root.val: return 1, 0
            if root.right:
                l, mr = mOrderHelper(root.right)
                if l > mr: return 1, 0
                if l <= root.val: return 1, 0
            return ml, mr

        a, b = mOrderHelper(root)
        return False if a > b else True
