class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        elif len(points) == 1:
            return 1

        points.sort()
        ans = [points.pop(0)]
        while points:
            if points[0][0] <= ans[-1][1]:
                ans[-1][0] = points[0][0]
                if points[0][1] < ans[-1][1]:
                    ans[-1][1] = points[0][1]
                points.pop(0)

            else:
                ans.append(points.pop(0))

        return len(ans)
