class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n%2==1:
            return nums[int((n-1)/2)]
        else:
            return nums[int(n/2)]