class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # mset = set()
        # nset = set()

        m = len(matrix)
        n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             mset.add(i)
        #             nset.add(j)

        # for i in mset:
        #     for j in range(n):
        #         matrix[i][j] = 0
        # for i in nset:
        #     for j in range(m):
        #         matrix[j][i] = 0

        colFlag = False
        for i in range(m):
            if matrix[i][0] == 0:
                colFlag = True
                break
        
        for i in range(n):
            if matrix[0][i] == 0:
                matrix[0][0] = 0
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0
        for i in range(1,n):
            if matrix[0][i] == 0:
                for j in range(1,m):
                    matrix[j][i] = 0

        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0

        if colFlag:
            for i in range(m):
                matrix[i][0] = 0        
