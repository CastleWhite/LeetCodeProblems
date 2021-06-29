class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        # columnNumber -= 1
        while columnNumber:
            n = columnNumber % 26
            columnNumber //= 26
            if n:
                res.append(chr(n-1+ord("A")))
            else:
                res.append('Z')
                columnNumber -= 1
            
        res.reverse()
        return "".join(res)
