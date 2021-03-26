class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left = 0
        right = l - 1

        while left <= right:
            f = nums[left]
            if f == target: return left

            i = (left + right) // 2
            mid = nums[i]
            if mid == target: return i

            if mid >= f:
                if target > f and target < mid:
                    left = left + 1
                    right = i - 1
                else:
                    left = i + 1
            else:
                if target > mid and target < f:
                    left = i + 1
                else:
                    left += 1
                    right = i - 1
        
        return -1
