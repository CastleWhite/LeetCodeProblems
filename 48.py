class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(n//2): # 每一圈 （从外到内）
            #j =  # 每边个数
            for j in range( n - 1 - i*2 ):
            # 四个边 顺时针旋转
                tmp = matrix[i][i+j]
                matrix[i][i+j] = matrix[n-1-i-j][i]
                matrix[n-1-i-j][i] = matrix[n-1-i][n-1-i-j]
                matrix[n-1-i][n-1-i-j] = matrix[i+j][n-1-i]
                matrix[i+j][n-1-i] = tmp
        return matrix
