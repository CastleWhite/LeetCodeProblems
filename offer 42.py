class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        
        maxc = [nums[0]]
        for i in range(1,l) :
            if maxc[i-1] < 0 :
                maxc.append(nums[i])
            else :
                maxc.append(nums[i] + maxc[i-1])

        return max(maxc)
