class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        st1 = []
        st2 = []
        res = [-1] * len(nums)
        for i, n in enumerate(nums):            
            while st2 and nums[st2[-1]] < n:
                res[st2.pop()] = n
            j = len(st1) - 1
            while j >= 0 and nums[st1[j]] < n:
                j -= 1
            st2.extend(st1[j+1:])
            del st1[j+1:]
            st1.append(i)
        return res

