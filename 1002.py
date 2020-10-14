class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        n = len(A)
        record = [[0]*n for _ in range(26)]
        
        for j in range(n): 
            for i in A[j]:
                record[ord(i)-ord('a')][j] += 1
                
        count = [min(zimu) for zimu in record]
        ans = []
        for i in range(26):
            for a in range(count[i]):
                ans.append(chr(ord('a')+i))
# chr()  ord()
        return ans
