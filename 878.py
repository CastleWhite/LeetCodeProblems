class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l, r = 2, min(a, b) * n
        c = lcm(a, b)
        def get(x: int) -> int:
            return x // a + x // b - x // c
        
        while l < r:
            mid = (l + r) >> 1
            th = get(mid)
            if th < n:
                l = mid + 1
            elif th >= n: 
                r = mid

        return r % (10**9+7)        
