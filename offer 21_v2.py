class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l = len(nums)-1
        while l > 0 and nums[l]%2 == 0:
            l = l - 1

        for i in range(1+l):
            if i >= l:
                return nums
            tmp = nums[i]
            if tmp%2 == 0 :
                nums[i] = nums[l]
                nums[l] = tmp
                while l > 0 and nums[l]%2 == 0:
                    l = l - 1
        return nums
