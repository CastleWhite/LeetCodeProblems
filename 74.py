class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i, j = 0, m-1
        while i <= j:
            mid = (i+j) // 2
            f = matrix[mid][-1]

            if f < target:
                i = mid + 1
            elif f > target:
                j = mid - 1
            else:
                return True
        if i >= m: return False

        mm = i
        i, j = 0, n-1
        while i <= j:
            mid = (i+j) // 2
            f = matrix[mm][mid]

            if f < target:
                i = mid + 1
            elif f > target:
                j = mid - 1
            else:
                return True
        
        return False
