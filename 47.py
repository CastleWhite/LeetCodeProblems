class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        def helper(chs, tmp):
            if not chs:
                ans.append(tmp)
                return
            
            for i in range(len(chs)):
                if i > 0 and chs[i] == chs[i-1]: continue
                helper(chs[:i]+chs[i+1:], tmp+[chs[i]])

        helper(nums, [])
        return ans
