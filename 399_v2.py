class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        n = len(equations)
        for i in range(n):
            a, b = equations[i]
            v = values[i]
            d[a].append([b,v])
            d[b].append([a,1/v])
        num_node = len(d)
        encode = list(d.keys())
        decode = {encode[i]:i for i in range(num_node)}
        res = [[-1]*num_node for _ in range(num_node)]
        for i in range(num_node):
            for j,v in d[encode[i]]:
                res[i][decode[j]] = v

        for k in range(num_node):
            for i in range(num_node):
                if (i == k): continue
                for j in range(num_node):
                    if (i == j) or (j == k): continue
                    if res[i][k]>0 and res[k][j]>0:
                        res[i][j] =  res[i][k] * res[k][j]

        ans = []
        for a, b in queries:
            if not a in d or not b in d: ans.append(-1.0)
            elif a == b: ans.append(1.0)
            else:
                ans.append(res[decode[a]][decode[b]])
        return ans
