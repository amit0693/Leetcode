class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a, n = [], len(nums)
        if target not in nums: return [-1,-1]
        a.append(nums.index(target))
        nums= nums[::-1]
        a.append(n -1-nums.index(target))
        return a 