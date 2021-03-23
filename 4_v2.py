class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        def getKmin(k):
                        
            l1 = l2 = 0
            while l1 < m and l2 < n and k > 1:
                i = j = (k) // 2 - 1
                newi = min(m-1, l1 + i)
                newj = min(n-1, l2 + j)
                if nums1[newi] <= nums2[newj]:
                    l1, k = newi + 1, k - (newi - l1 + 1)
                else:
                    l2, k = newj + 1, k - (newj - l2 + 1)

            if l1 == m:
                return nums2[l2 + k - 1]
            elif l2 == n:
                return nums1[l1 + k - 1]
            else:
                return min(nums2[l2], nums1[l1])

        if (m + n) % 2:
            return getKmin((m+n)//2 + 1)
        else:
            return (getKmin((m+n)//2 + 1) + getKmin((m+n)//2)) / 2
