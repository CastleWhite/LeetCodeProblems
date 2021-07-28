# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k: return [target.val]
        def find(target):
            res = []
            def dfs(node):
                if not node:
                    return False
                if node == target:
                    return True
                else:
                    res.append(node)
                    if dfs(node.left): return True
                    if dfs(node.right): return True
                    res.pop()
                    return False
            dfs(root)
            return res
        path = find(target)
        d = len(path)
        def layer(node, k):
            res = [node]
            for i in range(k):
                if not res: break
                new = []
                for n in res:
                    if n.left: new.append(n.left)
                    if n.right: new.append(n.right)
                res = new
            ans = [n.val for n in res]
            return ans
        res = []
        res += layer(target, k)
        for i in range(1,min(k,d+1)):
            if i == 1:
                if path[-1].left and path[-1].left != target:
                    res += layer(path[-1].left, k-2)
                elif path[-1].right and path[-1].right != target:
                    res += layer(path[-1].right, k-2)
            else:
                c = path[-i]
                if c.left and c.left != path[-i+1]:
                    res += layer(c.left, k-1-i)
                elif c.right and c.right != path[-i+1]:
                    res += layer(c.right, k-1-i)
        if d >= k: res.append(path[-k].val)
        return res



