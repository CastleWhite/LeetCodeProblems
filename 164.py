class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-1):
            diff = nums[i+1] - nums[i]
            if diff>ans:
                ans = diff
        return ans
