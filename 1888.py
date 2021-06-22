class Solution:
    def minFlips(self, s: str) -> int:
        l = len(s)
        even = [0,0]
        odd = [0,0]
        for i in range(0,l,2):
            if s[i] == '0':
                even[0] += 1
            else:
                even[1] += 1
        for i in range(1,l,2):
            if s[i] == '0':
                odd[0] += 1
            else:
                odd[1] += 1
        n_odd = l>>1
        n_even = l - n_odd
        opt = even[0] + odd[1]
        ans = min(opt, l-opt)
        if l%2:
            for i in range(l-1):
                if i%2:
                    if s[i] == '1': opt -= 1
                    else: opt += 1
                else:
                    if s[i] == '0': opt -= 1
                    else: opt += 1
                ans = min(ans, opt, l-opt)

        return ans
