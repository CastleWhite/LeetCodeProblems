class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        reco = [[] for _ in range(26)]
        l = len(S)
        for i in range(l):
            # reco[ord(i)-ord('a')] += 1
            reco[ord(S[i])-ord('a')].append(i)
        # print(reco)
        a = 0
        ans = []
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
        
