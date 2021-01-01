class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = -1
        r = -1
        le = len(flowerbed)
        ans = 0
        for i in range(le):
            if flowerbed[i]:
                r = i-1
                ans += (r-l)//2
                l = i+1

        if l<le-1:
            ans += (le - l)//2

        return ans>=n

