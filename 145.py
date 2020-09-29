# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        que = [[root, 0]]
        ans = []
        while que:
            node, count = que.pop()
            if count:
                ans.append(node.val)
            else:
                que.append([node, 1])
                if node.right:
                    que.append([node.right, 0])
                if node.left:
                    que.append([node.left, 0])

        return ans

