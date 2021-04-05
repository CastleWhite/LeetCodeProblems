class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = [[nums[0]]]

        for i in nums[1:]:
            l = len(ans[0])
            new_ans = []
            for a in ans:
                for j in range(l+1):
                    tmp = a.copy()
                    tmp.insert(j, i)
                    new_ans.append(tmp)
            ans = new_ans
        return ans



