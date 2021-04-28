class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tempArr = []
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                tempArr.append(nums1[i])
                i += 1
            else:
                tempArr.append(nums2[j])
                j += 1
        while i < m:
            tempArr.append(nums1[i])
            i += 1
        while j < n:
            tempArr.append(nums2[j])
            j += 1

        mid = (m + n) // 2
        if (m + n) % 2 == 0:
            return (tempArr[mid - 1] + tempArr[mid]) / 2

        return float(tempArr[mid])
