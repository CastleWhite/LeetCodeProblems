# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 哈希表？
        if not postorder:
            return None
        rootv = postorder[-1]
        root = TreeNode(rootv)
        for i in range(len(inorder)):
            if inorder[i] == rootv:
                l_inorder = inorder[0:i]
                r_inorder = inorder[i+1:]
                l_postorder = postorder[0:i]
                r_postorder = postorder[i:-1]
                break
        
        root.left = self.buildTree(l_inorder, l_postorder)
        root.right = self.buildTree(r_inorder, r_postorder)

        return root
