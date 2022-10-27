class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            if not i: return 0
            if i < 0: res = -res
        return res
