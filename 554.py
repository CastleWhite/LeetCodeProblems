class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        m = sum(wall[0])
        
        lit = dict()
        for _ in range(n):
            l = -1
            wall[_].pop()
            for i in wall[_]:
                l += i
                if l in lit:
                    lit[l] += 1
                else:
                    lit[l] = 1
        
        return n - max(lit.values()) if lit else n
