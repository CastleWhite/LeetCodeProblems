class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_head = 0
        l = len(nums)
        if l < 2:
            return

        for i in range(l):
            if nums[i] == 0:
                zero_head = i
                break
            if i == l-2:
                return

        for j in range(zero_head+1, l):
            if nums[j] != 0:
                nums[j], nums[zero_head] = nums[zero_head], nums[j]
                zero_head += 1
        return 
