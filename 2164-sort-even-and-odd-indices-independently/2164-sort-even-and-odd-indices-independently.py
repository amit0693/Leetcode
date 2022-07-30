
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        x = sorted([nums[x] for x in range(0, len(nums), 2)])
        y = sorted([nums[y] for y in range(1, len(nums), 2)], reverse=True)
        z = []
        for i in range(len(nums)//2+1):
            if i < len(x):
                z.append(x[i])
            if i < len(y):
                z.append(y[i])
        return z