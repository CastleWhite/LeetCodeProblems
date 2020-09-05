class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        jiec = [1]
        select = [1]
        for i in range(2,n+1):
            jiec.append(i*jiec[-1])
            select.append(i)
        ans = ""
        kk = k-1
        for i in range(n,1,-1):
            ans += str(select.pop(kk // jiec[i-2]))
            kk = kk % jiec[i-2]

        ans += str(select[0])
        return ans
