class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l = len(nums)
        left = 0
        right = l - 1

        while left <= right:
            f = nums[left]
            if f == target: return True

            i = (left + right) // 2
            mid = nums[i]
            if mid == target: return True
            if i == left: return target == mid or target == nums[right]

            if mid > f:
                if target > f and target < mid:
                    left = left + 1
                    right = i - 1
                else:
                    left = i + 1
            elif mid < f:
                if target > mid and target < f:
                    left = i + 1
                else:
                    left += 1
                    right = i - 1
            else:
                l_equal = True
                for a in range(left + 1, i):
                    if target == nums[a]: return True
                    if mid != nums[a]:
                        left = a + 1
                        right = i - 1
                        l_equal = False
                        break
                if l_equal:
                    left = i + 1
        
        return False
