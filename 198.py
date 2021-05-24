class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 3: return max(nums)

        m1, m2 = nums[0], max(nums[0], nums[1])
        for i in range(2,l):
            m1, m2 = m2, max(nums[i]+m1, m2)
        
        return m2
