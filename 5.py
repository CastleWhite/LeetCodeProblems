class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s)==1 or s==s[::-1]:
            return s

        def isPalindrome(l, r):  # return bool 
            if l<0:
                return False
            while l<r and s[l] == s[r]:
                l += 1
                r -= 1
            return l>=r

        reco = [1, s[0], True, True] # record [max_len, ans, max_at_end, all_same]
        for i in range(1,len(s)):
            # print(reco)
            if reco[2]: # 是否能加长 
            # 错误原因： 相等也行
                if reco[3] and s[i] == s[i-1]: # 特殊情况，轴可变
                    reco[0] += 1
                    reco[1] = s[i-reco[0]+1:i+1]
                elif i-reco[0]-1>=0 and s[i] == s[i-reco[0]-1]:
                    reco[0] += 2
                    reco[-1] = False
                    reco[1] = s[i-reco[0]+1:i+1]
                elif isPalindrome(i-reco[0]+1, i):
                    reco[1] = s[i-reco[0]+1:i+1]
                    reco[3] = reco[0]==1
                else: # 不能加长
                    reco[2] = False
            else:
                l = i-reco[0]
                if isPalindrome(l, i):
                    reco[0] += 1
                    reco[1] = s[l:i+1]
                    reco[2] = True
                    reco[3] = False
                else:
                    if isPalindrome(l+1, i):
                        reco[1] = s[l+1:i+1]
                        reco[2] = True
                        reco[3] = True
                        for a in s[l+1:i]:
                            if a != s[i]:
                                reco[3] = False
                                break
                    
        return reco[1]
        # 没必要记录这么多，只管长度即可

    # def longestPalindrome(self, s: str) -> str:
    #     if not s: return ""
    #     length = len(s)
    #     if length == 1 or s == s[::-1]: return s
    #     max_len,start = 1,0
    #     for i in range(1, length):
    #         add_1 = s[i-max_len:i+1]
    #         add_2 = s[i-max_len-1:i+1]
    #         if i - max_len - 1 >= 0 and add_2 == add_2[::-1]:
    #             start = i - max_len - 1
    #             max_len += 2
    #             continue
    #         if i - max_len >= 0 and add_1 == add_1[::-1]:
    #             start = i - max_len
    #             max_len += 1
    #             continue
    #     return s[start:start + max_len]

