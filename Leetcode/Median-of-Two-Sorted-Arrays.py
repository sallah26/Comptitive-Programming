class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        leng = len(nums1)
        if leng % 2 == 0:
            mid = leng // 2
            return ((nums1[mid] + nums1[mid-1]) /2 )
        else:
            mid = int(leng / 2)
            return nums1[mid]
