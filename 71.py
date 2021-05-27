class Solution:
    def simplifyPath(self, path: str) -> str:

        def read( begin, l):
            # return the next / loc
            while begin < l and path[begin] != '/':
                begin += 1
            return begin
        
        stack = []
        l = len(path)
        i = 0
        while i < l:
            nex = read(i, l)
            name = path[i:nex]
            if not name or name == '.':
                pass
            elif name == '..':
                if stack:
                    stack.pop()
            
            else:
                stack.append(name)
            i = nex + 1

        return '/'+'/'.join(stack)
