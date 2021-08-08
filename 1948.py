class node:
    def __init__(self):
        self.sons = dict()
        self.name = ""

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        #  build tree
        root = node()
        for path in paths:
            cur = root
            for n in path:
                if n in cur.sons:
                    cur = cur.sons[n]
                else:
                    s = node()
                    cur.sons[n] = s
                    cur = s
        # dfs get stru
        record = defaultdict(int)
        def dfs(r):
            tmp = []
            for i in r.sons:
                dfs(r.sons[i])
                tmp.append(i+'('+r.sons[i].name+')')
            tmp.sort()
            r.name = "".join(tmp)
            record[r.name] += 1
        dfs(root)
        # delete
        res = []
        pre = []
        def put(r):
            if record[r.name] > 1 and r.name != "":
                return
            
            res.append(pre.copy())
            for i in r.sons:
                pre.append(i)
                put(r.sons[i])
                pre.pop()
            return
        put(root)
        res.pop(0)
        return res
