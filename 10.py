class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        poss = {-1}
        l = len(s)
        lp = len(p)
        for n,i in enumerate(p):
            if n+1 < lp and p[n+1] == '*': continue

            new_poss = set()
            for loc in poss:
                if loc >= l-1:
                    if i == '*': new_poss.add(loc)
                    continue

                if i == s[loc+1]:
                    new_poss.add(loc+1)
                elif i == '.':
                    new_poss.add(loc+1)
                elif i == '*':
                    pre = p[n-1]
                    if pre == '.' or pre == '*':
                        for j in range(loc, l):
                            new_poss.add(j)
                    else:
                        new_poss.add(loc)
                        j = 1
                        while loc+j < l and s[loc+j] == pre:
                            new_poss.add(loc+j)
                            j += 1
                    
            if not new_poss:
                return False
            else:
                poss = new_poss
        
        if l-1 in poss: return True
        else: return False
