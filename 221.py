class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix[0])
        n = len(matrix)
        dp = [[0] * (m+1) for _ in range(n+1)]
        ans = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = 1 + min(dp[i][j+1], dp[i][j], dp[i+1][j])
                    ans = max(ans, dp[i+1][j+1])
        return ans**2
