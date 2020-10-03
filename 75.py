class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # if n<2:
        #     return None
        i = 0
        for _ in range(n):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0,0)
            elif nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                i -= 1
            i += 1
        
        return None
