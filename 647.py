class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        ans = 0
        for i in range(l):
            n = 0
            while i-n>=0 and i+n+1<l and s[i-n]==s[i+n+1]:
                n = n+1
            ans = ans + n
            
        for i in range(1,l):
            n = 1
            while i-n>=0 and i+n<l and s[i-n]==s[i+n]:
                n = n+1
            ans = ans + n-1

        return ans+l

