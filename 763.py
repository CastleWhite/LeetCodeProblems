class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        reco = [[] for _ in range(26)]
        l = len(S)
        for i in range(l):
            # 只需记录last即可，不用数组【-1】
            # for i, ch in enumerate(S):
            #   last[ord(ch) - ord("a")] = i
            reco[ord(S[i])-ord('a')].append(i)

        a = 0
        ans = []
        # 可以改用for 遍历
        while a < l:
            last = reco[ord(S[a])-ord('a')][-1]
            begin = a
            
            while last > a+1:
                temp = last
                for i in range(a+1, last):
                    b = reco[ord(S[i])-ord('a')][-1]
                    if b > last:
                        last = b
                a = temp

            ans.append(last - begin + 1)
            a = last + 1

        return ans
        
