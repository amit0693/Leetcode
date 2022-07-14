class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        lcm = 1
        for num in range(1, smallest + 1):
            if not largest % num  and not smallest % num:
                lcm = num 
                
        return lcm