# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         selfval. = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        def midOrder(root: TreeNode) -> List[int]:
            if not root:
                return []

            return midOrder(root.left)+[root.val]+midOrder(root.right)

        num = midOrder(root)
        
        for i in range(len(num)-1):
            num[i] = num[i+1] - num[i]
        num.pop()

        return min(num)
