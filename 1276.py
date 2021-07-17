class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices&1: return []
        t2 = tomatoSlices>>1
        t = t2 - cheeseSlices
        c = (cheeseSlices<<1) -t2
        if t < 0 or c < 0:
            return []
        else:
            return [t,c]
