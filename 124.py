# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        global ans
        ans = -inf

        def landrLength(root):
            l = r = 0
            if root.left: l = landrLength(root.left)
            if root.right: r = landrLength(root.right)
            global ans
            tmp = root.val
            if l > 0: tmp += l 
            if r > 0: tmp += r
            ans = max(ans, tmp)
            return root.val + max(l, r, 0)

        landrLength(root)
        return ans
