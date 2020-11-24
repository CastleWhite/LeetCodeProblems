# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:

        def countLayer(root: TreeNode) -> int:
            a = root
            ans = 0
            while a:
                ans += 1
                a = a.left
            return ans

        l = countLayer(root)
        if l == 0:
            return 0
        elif l == 1:
            return 1
        ans = []

        def helper(root: TreeNode, l: int):
            if l == 2:
                if root.right:
                    ans.append(1)
                else:
                    ans.append(0)
                return

            t = root.right
            for i in range(l-2):
                t = t.left
            if t:
                ans.append(1)
                helper(root.right, l-1)
            else:
                ans.append(0)
                helper(root.left, l-1)
            return

        helper(root, l)
        bot = 0
        for i in range(l-1):
            bot += ans[i] * 2**(l-2-i)

        return bot + 2**(l-1)




