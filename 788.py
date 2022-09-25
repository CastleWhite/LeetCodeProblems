class Solution:
    def rotatedDigits(self, n: int) -> int:
        n = [int(x) for x in str(n)]
        l = len(n)
        
        @cache
        def dfs(pos, limit, diff):
            if pos >= l: return 1 if diff else 0
            res = 0
            for i in range(10 if not limit else n[pos]+1):
                if i == 3 or i == 4 or i == 7: continue
                res += dfs(pos + 1, 1 if limit and i == n[pos] else 0, 1 if diff or i == 2 or i == 5 or i == 9 or i == 6 else 0)
            return res

        res = dfs(0, 1, 0)
        return res
