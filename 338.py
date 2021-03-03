class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        elif num == 1:
            return [0,1]
        
        ans = [0]+[1]*num
        p = 1
        n = 0
        for i in range(2,num+1):
            if n >= 2**p:
                n = 0
                p += 1

            ans[i] = ans[n] + 1
            n += 1

        return ans
