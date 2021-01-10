class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []

        begin = nums.pop(0)
        end = begin
        for i in nums:
            if i == end+1:
                end = i
            else:
                if begin==end:
                    ans.append(str(end))
                else:
                    ans.append(str(begin)+"->"+str(end))
                begin = i
                end = i
        if begin==end:
            ans.append(str(end))
        else:
            ans.append(str(begin)+"->"+str(end))

        return ans
