class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum=0
        s=set(nums)
        for i in s:
            if nums.count(i)==1:
                sum=sum+i
        return sum
