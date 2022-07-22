class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        x, n, m,  = [], len(nums1), len(nums2)
        for i in range(n):
            if nums1[i] in nums2 or nums1[i] in nums3:
                x.append(nums1[i])
        for i in range(m):
            if nums2[i] in nums1 or nums2[i] in nums3:
                x.append(nums2[i])
        return list(set(x))