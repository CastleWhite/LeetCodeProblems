# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root_val = root.val
        p_val = p.val
        q_val = q.val
        if (p_val-root_val)*(q_val-root_val)<=0:
            return root
        elif p_val-root_val>0:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)

        
