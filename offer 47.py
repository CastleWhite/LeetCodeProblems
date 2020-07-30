class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(n-1):
            grid[0][i+1] = grid[0][i]+grid[0][i+1]
        for i in range(1, m):
            grid[i][0] = grid[i-1][0]+grid[i][0]
            for j in range(n-1):
                grid[i][j+1] = max(grid[i][j],grid[i-1][j+1])+grid[i][j+1]
        
        return grid[-1][-1]
