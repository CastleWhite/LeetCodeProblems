class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        # def count(name: str) -> List:
        #     l = len(name)
        #     ans = []
        #     for i in range(l):
        #         if ans and name[i] == ans[-1][0]:
        #             ans[-1][1] += 1
        #         else:
        #             ans.append([name[i],1])
        #     return ans

        # n = count(name)
        # t = count(typed)
        # while n and t:
        #     nc = n.pop()
        #     tc = t.pop()
        #     if nc[0] != tc[0]:
        #         return False
        #     elif nc[1] <= tc[1]:
        #         continue
        #     else:
        #         return False
        # if n or t:
        #     return False
        # else:
        #     return True
# -------------------------------------------------------------
        # 双指针 更好?? 怎么更慢了

        ln = len(name)
        lt = len(typed)

        i = 0
        j = 0
        while i<ln and j<lt:

            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j>0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False
        if i == ln:
            while j < lt:
                if typed[j] == typed[j-1]:
                    j += 1
                else:
                    return False
            return True
        else:
            return False
