class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0: return 0
        elif l == 1: return 1
        nums.sort()

        ans = 1
        reco = 1
        for i in range(1,l):
            if nums[i] == nums[i-1]+1:
                reco += 1
            elif nums[i] == nums[i-1]:
                continue
            else: 
                ans = max(ans, reco)
                reco = 1

        return max(ans, reco)
