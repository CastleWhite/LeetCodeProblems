# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l = len(nums)
        if l == 0:
            return None
        elif l == 1:
            return TreeNode(nums[0])
            
        mid = floor(l/2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
