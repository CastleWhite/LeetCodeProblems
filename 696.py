class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = 0
        flag = s[0]
        count = 0
        ans = 0
        for i in s:
            if i == flag:
                n = n + 1
            else:
                ans = ans + min(n,count)
                count = n
                flag = i
                n = 1 
        ans = ans + min(n,count)
        return ans

