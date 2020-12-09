class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        # 回溯剪枝！！
        ll = len(S)
        uBound = 2**31-1
        def addStr(loc):
            cc = ans[-1] + ans[-2]
            if cc > uBound:
                return -1
            c = str(cc)
            # for i in c:
            #     if loc<ll and i == S[loc]:
            #         loc += 1
            #     else:
            #         return -1
            new_loc = loc+len(c)
            if new_loc>ll or S[loc:new_loc] != c:
                return -1
            ans.append(cc)
            return new_loc
        ans = []
        for two in range(2,min(20, ll-1)):  # 每个最多10位数 !! 这里改后，速度巨大提升 ！！
            for i in range(1,min(10, two)):
                a = S[0:i]
                b = S[i:two]
                if i>1 and a[0] == '0':
                    break
                elif two-i>1 and b[0] == '0':
                    continue
                ans = [int(a), int(b)]
                loc = two
                while loc < ll:
                    loc = addStr(loc)
                    if loc == -1:
                        break
                # print(i,two,loc)
                if loc == ll:
                    return ans
        return []
