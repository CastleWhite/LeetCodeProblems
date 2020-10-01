class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)

        f0 = 0
        if leaves[0] == 'y':
            f0 = 1

        f1 = f0    
        if leaves[1] == 'y':
            f0 += 1
        else:
            f1 += 1
        
        f2 = f1
        f1 = min(f1, f0)
        if leaves[2] == 'y':
            f0 += 1
            f2 += 1
        else:
            f1 += 1 

        for i in range(3,n):
            f1, f2 = min(f0, f1), min(f1, f2)
            
            if leaves[i] == 'y':
                f0 += 1
                f2 += 1
            else:
                f1 += 1
            
        return f2
