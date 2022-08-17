class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        a, n = [], len(nums)
        for i in range(n):
            a.insert(index[i], nums[i])
        return a