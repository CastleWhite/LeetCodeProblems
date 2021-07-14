class Solution:
    def numBusesToDestination(self, routes: List[List[int]], s: int, t: int) -> int:
        if s == t: return 0
        stops = defaultdict(list)
        for i, bus in enumerate(routes):
            for stop in bus:
                stops[stop].append(i)
        graph = [[] for _ in range(len(routes))]
        for i, bus in enumerate(routes):
            for stop in bus:
                graph[i].extend(stops[stop])
            graph[i] = set(graph[i])

        # visited = [0] * len(routes)
        stack = stops[s]
        d = [0] * len(routes)
        for i in stack:
            if i in stops[t]:
                return 1
            d[i] = 1
            
        while stack:
            bus = stack.pop(0)
            for i in graph[bus]:
                print(i)
                if i != bus and not d[i]:
                    stack.append(i)
                    d[i] = d[bus] + 1
                if i in stops[t]:
                    return d[i]
        return -1
