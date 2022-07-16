class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a= Counter(nums)
       
        for values in a.values():
            if values>=2:
                return True
            