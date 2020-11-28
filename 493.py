class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums: List[int]) -> (List[int], int):
            len_num = len(nums)
            if len_num < 2:
                return nums, 0
            mid = len_num // 2
            left, a1 = merge(nums[0:mid])
            right, a2 = merge(nums[mid:])
            l = 0
            r = 0
            ans_list = []
            ans = a1 + a2
            # while l < len(left) or r < len(right): # 试过统计和排序放不到一起
            #     if left[l] <= right[r]:
            #         ans_list.append(left[l])
            #         l += 1
            #     elif left[l] > 2*right[r]:
            #         ans += len(left) - l
            #         ans_list.append(right[r])
            #         r += 1
            #     else:
            #         ans_list.append(right[r])
            while l < mid and r < (len_num-mid): 
                if left[l] <= 2*right[r]:
                    l += 1
                else:
                    ans += mid - l
                    r += 1

            while left and right: 
                if left[0] <= right[0]:
                    ans_list.append(left.pop(0))
                else:
                    ans_list.append(right.pop(0))

            if not left:
                ans_list += right
            else:
                ans_list += left

            return ans_list, ans
        
        _, ans = merge(nums)
        return ans

