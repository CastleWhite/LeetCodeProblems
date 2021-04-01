class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lp = 1
        ans = [[], [nums[0]]]
        l = len(nums)
        for i in range(1, l):
            lans = len(ans)
            if nums[i] != nums[i-1]:
                for j in range(lans):
                    ans.append(ans[j]+[nums[i]])
            else:
                for j in range(lp, lans):
                    ans.append(ans[j]+[nums[i]])
                    
            lp = lans

        return ans
