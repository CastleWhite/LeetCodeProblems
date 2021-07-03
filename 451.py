class Solution:
    def frequencySort(self, s: str) -> str:
        n = 128
        count = [0] * n
        for c in s:
            count[ord(c)] += 1
        index = [i for i in range(n)]
        z = list(zip(count, index))
        z.sort(reverse=True)
        res = []
        for a in z:
            if not a[0]: break
            res.append(chr(a[1])*a[0])
        
        return "".join(res)
