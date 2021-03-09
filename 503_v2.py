class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        loc = []
        ans = [-1] * l


        for i in range(l * 2 - 1):
            while loc and (nums[loc[-1]] < nums[i % l]):
                ans[loc.pop()] = nums[i % l]
            if i < l:
                loc.append(i)

        return ans
