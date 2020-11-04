class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        a = newInterval[0]
        b = newInterval[1]
        l = len(intervals)

        left = 0
        right = l-1
        li = 0
        ln = a
        while left <= right:
            mid = (left+right)//2
            interval = intervals[mid]
            if interval[0] > a:
                right = mid - 1
                li = mid
            elif interval[1] < a:
                left = mid + 1
                li = left
            else:
                li = mid
                ln = interval[0]
                break
        
        left = li
        right = l-1
        ri = l - 1 
        rn = b
        while left <= right:
            mid = (left+right)//2
            interval = intervals[mid]
            if interval[0] > b:
                right = mid - 1
                ri = right
            elif interval[1] < b:
                left = mid + 1
                ri = mid
            else:
                ri = mid
                rn = interval[1]
                break
        
        return intervals[0:li] + [[ln,rn]] + intervals[ri+1:l]
