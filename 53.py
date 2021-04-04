class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = nums[0]

        for i in nums[1:]:
            if pre > 0:
                pre += i 
            else:
                pre = i
            ans = max(ans, pre)

        return ans
