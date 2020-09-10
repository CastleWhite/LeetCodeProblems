class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        if n < k or k<1:
            return []
        elif k == 1:
            for a in range(1,n+1):
                ans.append([a])
        elif n == k:
            ans = [list(range(1,n+1))]
        elif n > k:
            
            for j in range(n,0,-1):
                for i in self.combine(j-1,k-1):
                    if i:
                        i.append(j)
                        ans.append(i)

        return ans
