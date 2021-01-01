class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        ans = 0
        
        intervals.sort(key = lambda x: x[1])
        end = intervals.pop(0)[1]
        for i in intervals:
            if end > i[0]:
                ans+=1
            else:
                end = i[1]
            
        return ans
