class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] : return nums[0]
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] < nums[r] : return nums[l] # 用l判断，需要额外判断是否是有序数组
            # 用r则不必

            mid = (l+r) // 2
            if nums[l] == nums[mid]:
                # return self.findMin(nums[1:])，这个 慢很多
                l += 1
            elif nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid

        return nums[l] 
