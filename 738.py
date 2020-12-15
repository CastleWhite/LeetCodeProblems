class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        sn = str(N)
        pre = int(sn[0])
        ans = [pre]
        l = len(sn)

        def backtrack(i):
            if i == l:
                return True
            j = int(sn[i])
            if j >= ans[-1]:

                ans.append(j)
                if backtrack(i+1):
                    return True

                ans.pop(-1)
                if j-1 >= ans[-1]:
                    ans.append(j-1)
                    return True
            else:
                return False

        if backtrack(1):
            ans = list(map(str, ans))
            ll = len(ans)
            ans += ['9']*(l-ll)
            return int("".join(ans))
        else:
            return pre*10**(l-1)-1
            
