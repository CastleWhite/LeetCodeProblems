class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)>>1):
            m = nums[i] + nums[-1-i]
            ans = max(ans, m)
        return ans
