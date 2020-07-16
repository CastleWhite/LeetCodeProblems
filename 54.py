class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = matrix[0]
        m = len(matrix)
        n = len(ans)
        
        num = 1
        while 1:
            
            if num % 2:
                if num >= m:
                    return ans
                for i in range(m-num):
                    ans.append(matrix[num//2+1+i][n-1-num//2])
                if num >= n:
                    return ans
                for i in range(n-num):
                    ans.append(matrix[-1-num//2][n-2-num//2-i])
            else:
                if num >= m:
                    return ans
                for i in range(m-num):
                    ans.append(matrix[-1-num//2-i][num//2-1])
                if num >= n:
                    return ans
                for i in range(n-num):
                    ans.append(matrix[num//2][num//2+i])

            num = num + 1
