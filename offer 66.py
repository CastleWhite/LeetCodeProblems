class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        l = len(a)
        if l == 0:
            return []
        elif l == 1:
            return[0]
        left = [a[0]]
        right = [a[-1]]
        for i in range(1,l-1):
            left.append(left[i-1]*a[i])
            right.append(right[i-1]*a[l-1-i])
        ans = [right[-1]]
        for i in range(1,l-1):
            ans.append(left[i-1]*right[l-2-i])
        ans.append(left[-1])
        return ans
