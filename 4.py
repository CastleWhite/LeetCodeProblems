class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = -1
        j = -1
        ans1 = 0
        ans2 = 0
        while i < m-1 and j < n-1 and (i + j) < (m + n) // 2 - 1:
            if nums1[i+1] <= nums2[j+1]:
                i += 1
                ans1, ans2 = nums1[i], ans1
            else:
                j += 1
                ans1, ans2 = nums2[j], ans1

        if i == m-1:
            while (i + j) < (m + n) // 2 - 1:
                j += 1
                ans1, ans2 = nums2[j], ans1
        elif j == n-1:
            while (i + j) < (m + n) // 2 - 1:
                i += 1
                ans1, ans2 = nums1[i], ans1

        if (m + n) % 2:
            return ans1
        else:
            return (ans1 + ans2) / 2
