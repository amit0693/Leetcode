class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums) +2
        for i in range(n):
            if i not in nums:
                return i