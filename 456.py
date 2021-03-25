class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stacks = [[nums[0]]]
        
        l = len(nums)
        for i in range(1, l):
            a = nums[i]
            if a == nums[i-1]: continue

            new_stacks = []
            for stack in stacks:
                if len(stack) == 1:
                    if a > stack[0]:
                        stack.append(a)
                    else:
                        stack = [a]
                    new_stacks.append(stack)
                
                elif len(stack) > 1:
                    if a < stack[-1] and a > stack[0]:
                        return True
                    elif a >= stack[-1]:
                        new_stacks.append( [stacks[-1][0], a] )
                        break
                    elif a == stack[0]:
                        new_stacks.append( [stacks[-1][0], stack[-1]] )
                        break
                    else:
                        new_stacks.append(stack)

            if a < new_stacks[-1][0]:
                new_stacks.append( [a] )
            stacks = new_stacks
            # 更好方法： 二分查找；逆序。
        return False
