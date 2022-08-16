class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a, b, c = nums[:n], nums[n:], []
        n = len(a)
        for i in range(n):
            c.append(a[i])
            c.append(b[i])
        return c