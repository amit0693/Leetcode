class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=max(nums)
        nums.pop(nums.index(max(nums)))
        c=max(nums)
        return (a-1)*(c-1)
        