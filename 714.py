class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ans = 0
        begin = prices[0]
        flag = 1
        for i in prices[1:]:
            if flag>0:
                if i < begin:
                    begin = i
                elif i > begin + fee:
                    end = i
                    flag = -1
            else:
                if i > end:
                    end = i
                elif i <= end - fee:
                    ans += end - begin - fee
                    begin = i 
                    flag = 1
            
        if flag == -1:
            ans += end - begin - fee
        return ans
