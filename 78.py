class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for i in nums:
            l = len(ans)
            for j in range(l):
                ans.append(ans[j] + [i])
        
        return ans


