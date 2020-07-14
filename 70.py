class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1 
        else:
            a = 1
            b = 1
            for i in range(n-1):
                ans = a + b
                a = b
                b = ans
            return ans%1000000007
