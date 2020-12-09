class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 or n == 1:
        #     return 1
        # return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        # 递归 会超时

        # ans =[[1]*m] + [[0]*m for _ in range(n-1)]
        # for i in range(n):
        #     ans[i][0] = 1
        # for i in range(1,n):
        #     for j in range(1,m):
        #         ans[i][j] = ans[i-1][j] + ans[i][j-1]
        # return ans[n-1][m-1]
        # 迭代


        # 直接人为计算出 函数关系：组合
