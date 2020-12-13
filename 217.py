class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        di = dict()
        for i in nums:
            if i in di:
                return True
            else:
                di[i] = 1
        return False
