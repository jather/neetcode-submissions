class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength =  len(nums1) + len(nums2)
        half = totalLength // 2

        shorter, longer = nums1, nums2
        if len(nums2) < len(nums1):
            shorter, longer = nums2, nums1
        l, r = 0, len(shorter)
        #edge cases
        if len(shorter) == 0:
            if len(longer) % 2:
                return longer[half]
            else:
                return (longer[half] + longer[half - 1]) / 2
        while l <= r:
            m = (l + r) // 2
            m2 = half - m
            if m == 0 or shorter[m-1] <= longer[m2]:
                if m == len(shorter) or shorter[m] >= longer[m2 - 1]:
                    if totalLength % 2:
                        return min(shorter[m], longer[m2])
                    else:
                        if m == 0:
                            return (shorter[m] + longer[m2 - 1]) /2
                        if m == len(shorter):
                            return (shorter[m-1] + longer[m2]) /2
                        else:
                            lower = max(shorter[m-1], longer[m2-1])
                            higher = min(shorter[m], longer[m2])
                            return (higher + lower) / 2
                else:
                    l = m + 1
            else: r = m - 1
                    

        