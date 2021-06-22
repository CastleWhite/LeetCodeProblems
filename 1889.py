class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        ans = -1
        packages.sort(reverse=True)
        p_l = len(packages)
        p_sum = sum(packages)
        def qu(box: List[int]) -> int:
            box.sort(reverse=True)
            if box[0] < packages[0]: return -1
            res = -p_sum
            # 没有二分优化
            # for p in packages:
            #     while (box_i < l and box[box_i] >= p):
            #         box_i += 1
            #     if not box_i: return -1
            #     res += box[box_i-1] - p
            package_i = 0
            for box_i in range(1, len(box)):
                limit = box[box_i]
                l,r = package_i, p_l-1
                while l<=r:
                    mid = (l+r)>>1
                    if packages[mid] <= limit:
                        r = mid-1
                    else:
                        l = mid+1
                
                res += box[box_i-1] * (l-package_i)
                package_i = l
                if package_i == p_l: break
            res += box[-1] * (p_l - package_i)
            return res
        for box in boxes:
            res = qu(box)
            if res != -1: 
                if ans != -1:
                    ans = min(ans, res)
                else:
                    ans = res
        if ans == -1: return -1
        else:
            return ans%(10**9+7)
