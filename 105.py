# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None

        root = TreeNode(preorder[0])
        m = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                m = i
                break
        # 改进：
        # 构造哈希映射，快速定位根节点        
        root.left = self.buildTree(preorder[1:m+1], inorder[0:m])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        # 改进：
        # 构造helper函数，参数为index,不需要复制数组  

        return root
        
