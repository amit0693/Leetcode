class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k=set(nums)
        count=1
        while count in k:
            count+=1
        return count