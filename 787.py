class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        m = len(flights)
        to, ne, h, w = [-1] * m, [-1] * m, [-1] * n, [-1] * m
        i = 0
        for f in flights:
            w[i] = f[2]
            to[i] = f[1]
            ne[i] = h[f[0]]
            h[f[0]] = i
            i += 1

        inf = 1000010
        q = [inf] * n
        q[src] = 0
        i = h[src]
        while i != -1:
            q[to[i]] = w[i]
            i = ne[i]
        dist = q[:]   
        for _ in range(k):              
            for j in range(n):
                if q[j]<inf:
                    i = h[j]                    
                    while i != -1:
                        dist[to[i]] = min(q[j]+w[i], dist[to[i]])
                        i = ne[i]
            q = dist[:]
        
        return q[dst] if q[dst] < inf else -1
