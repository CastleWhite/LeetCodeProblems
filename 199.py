# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [root]

        res = []
        # layer 
        while stack:
            n = TreeNode()
            for i in range(len(stack)):
                n = stack.pop(0)
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            res.append(n.val)
        
        return res
