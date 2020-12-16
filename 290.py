class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()
        l = len(pattern)
        ll = len(ss)
        if l != ll:
            return False
        d = {}
        dd = {}
        for i in range(l):
            if pattern[i] in d:
                if d[pattern[i]] != ss[i]:
                    return False
            elif ss[i] in dd:
                return False
            else:
                d[pattern[i]] = ss[i]
                dd[ss[i]] = pattern[i]
        return True
