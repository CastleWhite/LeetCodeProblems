class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)

        reco = nums[0:2]
        reco.append(nums[0]+nums[2])
        for i in range(3,len(nums)-1):
            reco.append(nums[i] + max(reco[i-2], reco[i-3]))
        ans = max(reco[-1], reco[-2])

        reco = nums[0:3]
        reco[0] = 0
        for i in range(3,len(nums)):
            reco.append(nums[i] + max(reco[i-2], reco[i-3]))
        ans = max(reco[-1], reco[-2], ans)

        return ans
