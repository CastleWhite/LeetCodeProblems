class Solution:
    def isValid(self, s: str) -> bool:
        left = {'[','{','('}
        right = {']': '[', '}': '{', ')': '('}
        a = []
        for i in s:
            if i in left:
                a.append(i)
            else:
                if not a:
                    return False
                if right[i] != a[-1]:
                    return False
                else :
                    a.pop()
        return not a

