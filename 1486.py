class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i  in range(n):
            num = start+2*i
            ans = ans ^ num

        return ans
