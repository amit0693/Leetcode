class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        a = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                a.append(count)
            elif nums[i] == 0:
                count = 0
        return max(a) if len(a)!= 0 else 0
        