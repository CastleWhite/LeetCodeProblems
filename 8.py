class Solution:
    def myAtoi(self, s: str) -> int:
        l = len(s)
        n = 0
        flag = True
        ans = 0

        while (n < l and s[n] == ' '):
            n += 1

        if n >= l:
            return 0
        elif s[n] == '-':
            flag = False
            n += 1
        elif s[n] == '+':
            n += 1

        while (n < l and s[n] >= '0' and s[n] <= '9'):
            ans = ans*10 + int(s[n])
            n += 1


        if flag:
            if ans < 2**31:
                return ans
            else: return 2**31-1
        else:
            if ans <= 2**31:
                return -ans
            else: return -2**31

