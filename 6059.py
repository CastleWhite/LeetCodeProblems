# DFS + 剪枝
# 0x3f

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ')' or grid[-1][-1] == '(' or (m + n - 1) & 1: return False

        @cache
        def dfs(i, j, c):
            if c > (m - i + n - j - 1): return False
            if i == m - 1 and j == n - 1: return c == 1

            c += -1 if grid[i][j] == ')' else 1
            if c < 0: return False
            return i < m - 1 and dfs(i + 1, j, c) or j < n - 1 and dfs(i, j + 1, c)

        return dfs(0, 0, 0)
