class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, c in edges:
            g[u].append((v, c+1))
            g[v].append((u, c+1))
        
        def dji(g):
            dist = [10**9] * n 
            dist[0] = 0
            h = []
            heappush(h, (0, 0))
            while h:
                l, d = heappop(h)
                if l > dist[d]: continue
                for i, c in g[d]:
                    new_l = c + dist[d]
                    if new_l < dist[i]:
                        dist[i] = new_l
                        heappush(h, (new_l, i))
            return dist

        dist = dji(g)
        res = 0
        for i in range(n):
            if dist[i] <= maxMoves:
                res += 1
        for u, v, c in edges:
            tmp = 0
            if dist[u] < maxMoves:
                tmp += maxMoves - dist[u]
            if dist[v] < maxMoves:
                tmp += maxMoves - dist[v]
            res += min(c, tmp)

        return res
