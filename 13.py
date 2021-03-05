class Solution:
    def romanToInt(self, s: str) -> int:
        record = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        l = len(s)
        if l <= 1:
            return record[s]
        
        pre = record[s[0]]
        i = 1
        ans = 0
        while i < l:
            if record[s[i]]>pre:
                ans -= pre
            else:
                ans += pre
            pre = record[s[i]]
            i += 1
        return record[s[-1]] + ans
