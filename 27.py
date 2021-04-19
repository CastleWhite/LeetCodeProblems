class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        f = 0
        for n,i in enumerate(nums):
            if i != val:
                nums[f] = i
                f += 1
        
        return f
