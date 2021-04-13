# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = []

        stack = [root]
        while stack:
            new_stack = []
            layer = []
            for n in stack:
                layer.append(n.val)
                if n.left: new_stack.append(n.left)
                if n.right: new_stack.append(n.right)
            stack = new_stack
            ans.append(layer)
        
        return ans
