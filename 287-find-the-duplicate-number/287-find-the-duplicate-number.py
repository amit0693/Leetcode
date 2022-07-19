class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = Counter(nums)
        for x,y in Counter(nums).items():
            if y >= 2:
                return x