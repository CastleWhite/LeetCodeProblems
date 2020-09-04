# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if root.right == None and root.left == None:
            return [str(root.val)]
        else:
            ans = []
            if root.right:
                ans += ( str(root.val) + "->" + i for i in self.binaryTreePaths(root.right))
            if root.left:
                ans += ( str(root.val) + "->" + i for i in self.binaryTreePaths(root.left))
            
            return ans
