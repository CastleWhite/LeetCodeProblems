class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]
        r = len(nums) - 1 
        l = 0

        while r >= l:
            if r <= l+1: return nums[r]
            mid = (l+r) // 2

            if nums[mid] > nums[l]:
                l = mid 
            else:
                r = mid 

        return nums[l]

            
