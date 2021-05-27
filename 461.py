class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sum = x ^ y
        res = 0
        while sum:
            sum = sum & (sum-1)
            res += 1
        
        return res
