class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        a=[]
        count =0
        for i in nums:
            if target == i:
                a.append(count)
            count += 1
        return a
        