class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        reco = [0, 0]
        ans = 0

        for i in nums:
            if i > 0:
                if reco[0] == 0:
                    reco[0] = i
                else:
                    reco[0] = i*reco[0]
                reco[1] = i*reco[1]
                ans = max(ans, reco[0])
            elif i == 0:
                reco = [0, 0]
            else:
                if reco[0] == 0:
                    reco[0] = i*reco[1]
                    reco[1] = i
                else:
                    reco[0], reco[1] = i*reco[1], i*reco[0]
                ans = max(ans, reco[0])

        return ans
