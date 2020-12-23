class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        if not 1 in c.values(): 
            return -1
        for i,n in enumerate(s):
            if c[n] == 1:
                return i

