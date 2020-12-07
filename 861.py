class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        reco = [0]*m
        ans = n* 2**(m-1)
        for i in range(n):
            if A[i][0] == 0:
                for j in range(m):
                    A[i][j] = 1 - A[i][j]
            for j in range(m):
                reco[j] += A[i][j]
        # 处理第一位-------------统计后面位
        for i in range(1,m):
            if reco[i] < (n+1)//2:
                ans += (n - reco[i])* 2**(m-1-i)
            else:
                ans += reco[i]* 2**(m-1-i)
        # 处理后面位
        return ans
