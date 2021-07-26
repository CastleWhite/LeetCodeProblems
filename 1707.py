class trie:
    left = None
    right = None

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        n = len(nums)
        # 离线查
        stored = defaultdict(list)
        for i, (x, m) in enumerate(queries):
            stored[m].append((x, i))
        order = list(stored.keys())
        order.sort()

        MAX = 30
        root = trie()
        def add(n):
            cur = root
            for k in range(MAX, -1, -1):
                if (n >> k) & 1:
                    if not cur.right:
                        cur.right = trie()
                    cur = cur.right
                else:
                    if not cur.left:
                        cur.left = trie()
                    cur = cur.left
        def find(x):
            res = 0
            cur = root
            for k in range(MAX, -1, -1):
                res <<= 1
                if (x >> k) & 1:
                    if cur.left:
                        cur = cur.left
                        res += 1
                    else:
                        cur = cur.right
                else:
                    if cur.right:
                        cur = cur.right
                        res += 1
                    else:
                        cur = cur.left
            return res

        ni = 0
        res = [-1] * len(queries)
        for m in order:
            while ni < n and nums[ni] <= m:
                add(nums[ni])
                ni += 1
            for x, i in stored[m]:
                if root.left or root.right:
                    res[i] = find(x)
                else:
                    res[i] = -1
        return res


