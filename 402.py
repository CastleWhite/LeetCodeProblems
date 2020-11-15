class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 该用单调栈的，只要小，就可以丢
        if k == len(num):
            return "0"
        
        def removeKdigits2(num:str, k:int) :
            l = len(num)
            if k == l:
                return ""
            elif k==0:
                return num
            else:
                option = num[0:k+1]
                m = min(option)
                
                for i,n in enumerate(option):
                    if n==m:
                        return str(m) + removeKdigits2(num[i+1:], k-i) 
                
        ans = removeKdigits2(num, k)
        while (len(ans) > 1) and (ans[0] == "0"):
            ans = ans[1:]
            
        return ans
