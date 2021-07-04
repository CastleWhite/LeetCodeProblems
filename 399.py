class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        n = len(equations)
        for i in range(n):
            a, b = equations[i]
            v = values[i]
            d[a].append([b,v])
            d[b].append([a,1/v])
        
        def bfs(a, b):
            if not (a in d and b in d):
                return -1.0
            if a == b:
                return 1.0
            stack = [a]
            v_tmp = [1]
            visited = [a]
            while stack:
                node = stack.pop(0)
                v = v_tmp.pop(0)
                for comb in d[node]:
                    if comb[0] == b:
                        return v*comb[1]
                    elif not comb[0] in visited:
                        stack.append(comb[0])
                        v_tmp.append(v*comb[1])
                        visited.append(comb[0])
            return -1.0
        res = []
        for q in queries:
            res.append(bfs(q[0],q[1]))
        return res
