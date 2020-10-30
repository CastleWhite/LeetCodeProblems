class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        max_m = len(grid)-1
        max_n = len(grid[0])-1
        for m,line in enumerate(grid):
            
            for n,ge in enumerate(line):
                if ge:
                    ans += 4
                    if m != 0 and grid[m-1][n]:
                        ans -= 1
                    if m != max_m and grid[m+1][n]:
                        ans -= 1
                    if n != 0 and grid[m][n-1]:
                        ans -= 1
                    if n != max_n and grid[m][n+1]:
                        ans -= 1


        return ans
