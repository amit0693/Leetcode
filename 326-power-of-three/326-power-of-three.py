class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        count = 1
        while(count<n):
            count = count * 3
        return count == n