class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        a = 0
        for i in nums:
            if i != nums[a]:
                a += 1
                nums[a] = i
            
        return a+1
