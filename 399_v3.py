class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(a):
            if d[a] == []:
                d[a] = [-1, 1]
                return a, 1
            elif isinstance(d[a][0], int):
                return a, 1
            else:
                f, v = find(d[a][0])
                d[a] = [f, v*d[a][1]]
                return d[a]
        def union(a, b, v):
            fa, va = find(a)
            fb, vb = find(b)
            if fa == fb:
                return
            if d[fa][0] < d[fb][0]:
                d[fa][0] += d[fb][0]
                d[fb] = [fa, va*v/vb]
            else:
                d[fb][0] += d[fa][0]
                d[fa] = [fb, vb/v/va]
            
        d = defaultdict(list)
        n = len(equations)
        for i in range(n):
            a, b = equations[i]
            v = values[i]
            union(a, b, v)
# 用map不用数组，无需encode

        ans = []
        for a, b in queries:
            if not a in d or not b in d: ans.append(-1.0)
            elif a == b: ans.append(1.0)
            else:
                fa, va = find(a)
                fb, vb = find(b)
                if fa != fb: ans.append(-1.0)
                else:
                    ans.append(vb/va)
        return ans
