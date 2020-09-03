class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        a = [nums]
        for i in range(N-1,0,-1):
            b = []
            for j in range(i):
                b.append(max(nums[N-i+j]-a[-1][j], nums[j]-a[-1][j+1]))
            a.append(b)

        return a[-1][0] >= 0
