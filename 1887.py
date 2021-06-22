class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        s = sorted(set(nums), reverse=True)
        res = 0
        s.pop()
        pre = 0
        for i in s:
            res = res+count[i]+pre
            pre += count[i]
        return res
