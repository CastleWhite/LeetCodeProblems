class tire:
    left = None
    right = None
    cnt = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        sons = defaultdict(list)
        root = -1
        for n, i in enumerate(parents):
            if i == -1: root = n
            else:
                sons[i].append(n)
        q = defaultdict(list)
        for i, (n, v) in enumerate(queries):
            q[n].append((v, i))
        res = [0] * len(queries)

        t = tire()
        Max = 18
        def add(n):
            t.cnt += 1
            cur = t
            for k in range(Max, -1, -1):
                if (n>>k) & 1:
                    if not cur.right:
                        cur.right = tire()
                    cur = cur.right
                else:
                    if not cur.left:
                        cur.left = tire()
                    cur = cur.left
                cur.cnt += 1

        def delete(n):
            t.cnt -= 1
            cur = t
            for k in range(Max, -1, -1):
                if (n>>k) & 1:
                    cur = cur.right
                else:
                    cur = cur.left
                cur.cnt -= 1

        def get(value):
            cur = t
            res = 0
            for k in range(Max, -1 ,-1):
                res <<= 1
                if (value>>k) & 1:
                    if cur.left and cur.left.cnt:
                        cur = cur.left
                        res += 1
                    else:
                        cur = cur.right
                else:
                    if cur.right and cur.right.cnt:
                        cur = cur.right
                        res += 1
                    else:
                        cur = cur.left
            return res

        def dfs(node):
            add(node)
            for v, i in q[node]:
                res[i] = get(v)
            for son in sons[node]:
                dfs(son)
            delete(node)
        dfs(root)
        return res
