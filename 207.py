class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)] 
        pre = [0] * numCourses
        for a,b in prerequisites:
            adjList[b].append(a) 
            pre[a] += 1
        
        queue0 = [i for i in range(numCourses) if not pre[i]]
        while queue0:
            c = queue0.pop()
            for hou in adjList[c]:
                pre[hou] -= 1
                if not pre[hou]: queue0.append(hou)
        
        return not sum(pre)
