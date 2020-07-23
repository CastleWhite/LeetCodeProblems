class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1, m+n-1):
            for x in range(max(0,i-m+1), min(i+1,n)):
                y = i-x
                
                if x == 0:
                    grid[y][x] = grid[y][x] + grid[y-1][x]
                elif y == 0:
                    grid[y][x] = grid[y][x] + grid[y][x-1]
                else:
                    grid[y][x] = grid[y][x] + min(grid[y-1][x], grid[y][x-1]) 
        return grid[-1][-1]
