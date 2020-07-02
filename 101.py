# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, p: TreeNode, q: TreeNode) -> bool:
        if p.val != q.val:
            return False
        else:
            if p.left == None:
                if q.right != None:
                    return False
                else:
                    if p.right == None:
                        return q.left == None
                    else:
                        if q.left == None:
                            return False
                        else:
                            return self.isMirror(p.right, q.left)
            else:
                if q.right == None:
                    return False
                else:
                    if p.right == None:
                        if q.left != None:
                            return False
                        else:
                            return self.isMirror(p.left, q.right)
                    else:
                        if q.left == None:
                            return False
                        else:
                            return self.isMirror(p.right, q.left) and self.isMirror(p.left, q.right)

            
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
            
        if root.left == None:
            return root.right == None
        elif root.right == None:
            return False
        else:
            return self.isMirror(root.left, root.right)
