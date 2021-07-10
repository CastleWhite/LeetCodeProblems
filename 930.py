class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = len(nums)
        for i in range(1,l):
            nums[i] += nums[i-1]
        nums.insert(0, 0)
        left , right= 0, 1
        res = 0
        for i in range(1,l+1):
            while nums[i] - nums[left] > goal and left<i:
                left += 1
            if left == i or nums[i] - nums[left] < goal:
                continue
            if left>right:
                right = left+1
            while nums[right]==nums[left] and right<i:
                right += 1
            res += right-left
        
        return res

                
