class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stacks = [[nums[0]]]
        
        l = len(nums)
        for i in range(1, l):
            a = nums[i]
            if a == nums[i-1]: continue

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
                    break
                
                elif len(stack) > 1:
                    if a < stack[-1] and a > stack[0]:
                        return True
                    elif a > stack[-1]:
                        right = j - 1
                    elif a < stack[0]:
                        left = j + 1
                    else: 
                        tmp = [stacks[-1][0], stack[-1]]
                        for _ in range(ls-j):
                            stacks.pop()
                        stacks.append( tmp )
                        break
            if right < 0:
                stacks = [[stacks[-1][0], a]]
            elif left >= ls:
                stacks.append( [a] )
                
            elif right < left:
                tmp = [stacks[-1][0], a]
                for _ in range(ls-left):
                    stacks.pop()
                stacks.append( tmp )

            # 更好方法： 逆序。
        return False
