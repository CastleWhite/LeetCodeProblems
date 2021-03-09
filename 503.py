class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        v = []
        loc = []
        ans = [-1] * l

        for _ in range(2):
            for i in range(l):
                while v and (v[-1] < nums[i]):
                    ans[loc[-1]] = nums[i]
                    v.pop()
                    loc.pop()
                v.append(nums[i])
                loc.append(i)

        return ans
