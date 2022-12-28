class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s)-1
        while i < j and s[i] == s[j]:
            tmp = s[i]
            while i <= j and s[i] == tmp:
                i += 1
            while i <= j and s[j] == tmp:
                j -= 1
        return j-i+1
