class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        T = (numRows-1)*2
        # 0      /   0+T ...
        # 1 ;T-1 /   1+T T-1+T ...
        # 2 ;T-2 /
        # T/2    /
        l = len(s)
        n = (l+T-1) // T 

        ans = ""
        for i in range(n):
            ans += s[i*T]
        for j in range(1,(numRows-1)):
            for i in range(n-1):
                ans += s[j+i*T]
                ans += s[T-j+i*T]

            if j+n*T-T < l:
                ans += s[j-T+n*T]
                if -j+n*T < l:
                    ans += s[-j+n*T]
        for i in range(n-1):
            ans += s[(numRows-1)+i*T]
        if (numRows-1)+n*T-T < l:
            ans += s[(numRows-1)-T+n*T]

        return ans
