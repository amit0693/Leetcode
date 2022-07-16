class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        total, cnt1, cnt2 = [], collections.Counter(nums1), collections.Counter(nums2)
        print(cnt1, cnt2)
        for k, v in cnt1.items():
            if k in cnt2 and cnt2:
                total.append(k)
                
        return total
        