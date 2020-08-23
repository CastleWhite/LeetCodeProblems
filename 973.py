class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        r = []
        for i in range(len(points)):
            l = points[i][0]*points[i][0] + points[i][1]*points[i][1]
            r.append((l,i))
        heapify(r) 
        # 堆的规模太大
        ans = []
        for a in range(K):
            m,i = heappop(r)
            ans.append(points[i])
        return ans
