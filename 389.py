class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(t)
        c.subtract(s)
        a = c.most_common(1)
        ans, count = a[0]
        return ans
