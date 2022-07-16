class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            ind = nums2.index(i)
            for j in nums2[ind:]:
                if(j>i):
                    flag = (j)
                    break
                else:
                    flag = -1
            res.append(flag)
        return(res)