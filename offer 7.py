# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        rootv = preorder[0]
        root = TreeNode(rootv)

        locat = 0
        for i in range(len(inorder)):
            if inorder[i] == rootv:
                locat = i
                break
        ltree = inorder[0: locat]
        rtree = inorder[locat+1: ]
        
        ltree_pre = preorder[1: 1+locat]
        rtree_pre = preorder[1+locat: ]
        root.left = self.buildTree(ltree_pre, ltree)
        root.right = self.buildTree(rtree_pre, rtree)
        return root
