# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> (bool, List[List[int]]):
        if not root:
            return False, []
        
        val = sum - root.val
        if root.left or root.right:         
            b1, road = self.hasPathSum(root.left, val)                
            b2, road2 = self.hasPathSum(root.right, val)
            if b1 and b2:
                ans = road + road2
                for i in ans:
                    i.insert(0, root.val)
                return True, ans
            elif b1:
                for i in road:
                    i.insert(0, root.val)
                return True, road
            elif b2:
                for i in road2:
                    i.insert(0, root.val)
                return True, road2
            else:
                return False, []
        else:
            return not val, [[root.val]]
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        b, road = self.hasPathSum(root, sum) 
        if b:
            return road
        else:
            return []

