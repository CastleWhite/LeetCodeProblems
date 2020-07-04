# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if (not root):
            return []
        ans = []
        q = []
        q.append(root)
        while q:
            p = []
            layer = []
            while q:
                temp = q.pop(0)
                layer.append(temp.val)
                
                if temp.left:
                    p.append(temp.left)
                if temp.right:
                    p.append(temp.right)

            q = p
            ans.append(layer)
        ans.reverse()
        return ans
