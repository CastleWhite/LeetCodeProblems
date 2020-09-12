# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def nextLevel(levelList: List[TreeNode]) -> {List[TreeNode],float}:
            ans = []
            sum = 0
            l = len(levelList)
            for i in levelList:
                sum += i.val
                if i.left:
                    ans.append(i.left)
                if i.right:
                    ans.append(i.right)
            return ans, sum/l
        level = [root]
        ans = []
        while level:
            level, v = nextLevel(level)
            ans.append(v)
        
        return ans


