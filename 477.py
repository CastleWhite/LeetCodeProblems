class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        l = len(nums)
        res = 0
        for _ in range(30):
            one = 0
            for i in range(l):
                if nums[i] & 1:
                    one += 1
                nums[i] = nums[i] >> 1
            res += one*(l-one)
        
        return res
