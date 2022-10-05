class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)
        for i in cpdomains:
            n, name = i.split(' ')
            subi = name.split('.')
            for j in range(len(subi)):
                k = '.'.join(subi[j:])
                res[k] += int(n)
        ans = []
        for k, v in res.items():
            ans.append(str(v) + ' ' + k)

        return ans
