class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n, a in enumerate(nums):
            if nums[abs(a)-1] < 0:
                res.append(abs(a)) 
            else:
                nums[abs(a)-1] = -nums[abs(a)-1]
        return res
