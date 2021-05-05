class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        n = sorted(c)

        point = [[-1,0],[0,0]]
        for i in n:
            tmp = 0
            x = -1
            if point[x][0] + 1 == i:
                tmp = point[x][1]
                x = -2
            new_point = max(point[x][1] + c[i]*i, tmp)
            point.append([i, new_point])
        
        return point[-1][1]
