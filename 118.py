class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            ans = [[1], [1,1]] 
            for i in range(1, numRows-1):
                new = []
                for j in range(i):
                    new.append(ans[-1][j] + ans[-1][j+1])
                new = [1] + new + [1]
                ans.append(new)
            return ans
