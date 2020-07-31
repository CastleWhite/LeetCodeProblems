class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        start = 0
        mid = l//2
        while start < l-1:
            if nums[mid] == mid:
                start = mid + 1
                
            else :
                l = mid
            mid = (start + l) // 2
        if start != l and nums[start] == start:
            return l
        else:
            return start
