class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums.extend([-1, -1])
        l = len(nums)
        for i in range(l):
            while nums[i] != i+1 and nums[i] != -1:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
        res = []
        for i in range(l):
            if nums[i] == -1: res.append(i+1)
        return res
