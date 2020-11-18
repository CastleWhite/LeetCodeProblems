class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        jin = []
        option = []
        for i in range(l):
            j = gas[i]-cost[i] 
            jin.append(j)
            if j >= 0:
                option.append(i)

        def ok(i: int) -> bool:
            init = 0
            for loc in range(i,i+l):
                loc = loc % l
                init += jin[loc]
                if init < 0:
                    return False
            return True

        if not option:
            return -1
        else:
            for i in option:
                if ok(i):
                    return i
            return -1
