class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stacks = [[nums[0]]]
        
        l = len(nums)
        for i in range(1, l):
            a = nums[i]
            if a == nums[i-1]: continue

            new_stacks = []
            ls = len(stacks)
            left = 0
            right = ls - 1
            while left <= right:
                j = (left+right)//2
                stack = stacks[j]

                if len(stack) == 1:
                    if a > stack[0]:
                        stacks[-1].append(a)
                    else:
                        stacks[-1] = [a]
                    new_stacks = stacks
                    break
                
                elif len(stack) > 1:
                    if a < stack[-1] and a > stack[0]:
                        return True
                    elif a > stack[-1]:
                        right = j - 1
                    elif a < stack[0]:
                        left = j + 1
                    else: 
                        new_stacks = stacks[0:j]
                        new_stacks.append( [stacks[-1][0], stack[-1]] )
                        break
            if right < 0:
                new_stacks = [[stacks[-1][0], a]]
            elif left >= ls:
                stacks.append( [a] )
                new_stacks = stacks
            elif right < left:
                new_stacks = stacks[0:left]
                new_stacks.append( [stacks[-1][0], a] )

            stacks = new_stacks
            # 更好方法： 逆序。
        return False
