class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.record = matrix
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            for i in range(1,n):
                self.record[0][i] += self.record[0][i-1]
            for i in range(1,m):
                self.record[i][0] += self.record[i-1][0]
                for j in range(1,n):
                    self.record[i][j] += self.record[i-1][j]+self.record[i][j-1]-self.record[i-1][j-1]




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.record[row2][col2]
        elif row1 == 0:
            return self.record[row2][col2] - self.record[row2][col1-1]
        elif col1 == 0:
            return self.record[row2][col2] - self.record[row1-1][col2]
        else:
            return self.record[row2][col2] - self.record[row1-1][col2] - self.record[row2][col1-1] + self.record[row1-1][col1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
