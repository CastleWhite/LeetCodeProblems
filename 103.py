# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        ans = []
        left = False
        while stack:
            l = len(stack)
            nextLayer = []
            layer = []
            for i in range(l-1, -1, -1):
                tmp = stack[i]
                layer.append(tmp.val)
                if left:
                    if tmp.right:
                        nextLayer.append(tmp.right)
                    if tmp.left:
                        nextLayer.append(tmp.left)
                else:
                    if tmp.left:
                        nextLayer.append(tmp.left)
                    if tmp.right:
                        nextLayer.append(tmp.right)
            ans.append(layer)
            stack = nextLayer
            left = not left
        
        return ans



